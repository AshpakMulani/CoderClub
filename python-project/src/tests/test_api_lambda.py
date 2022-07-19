from msilib.schema import tables
from xml.dom import ValidationErr
import boto3
import pytest
import os
from moto import mock_dynamodb

from src.api_lambda import (
    get_table_name,
    get_table_region,
    extract_event,
    prepare_response,
    get_dynamo_db_resource,
    get_dynamodb_table,
    user_post_handler,
    lambda_handler
)


def test_lambda_handler_success(dynamodb_table):     
    event = {
        "path": "/user", "httpMethod": "POST",    
        "queryStringParameters": {"name": "sample_user_name" }
            }   
    
    resp = lambda_handler(event, None)      

    assert resp['statusCode'] == 200  
    assert resp['body'] == 'user added successfully'
    
def test_lambda_handler_validation_failure(dynamodb_table):
    event = {
        "path": "/user", "httpMethod": "POST",    
        "queryStringParameters": { }
            }   
    
    resp = lambda_handler(event, None)      

    assert resp['statusCode'] == 400  
    assert resp['body'] == 'invalid query arguments'

def test_lambda_handler_wrong_path(dynamodb_table):     
    event = {
        "path": "/user/wrongpath", "httpMethod": "POST",    
        "queryStringParameters": {"name": "sample_user_name" }
            }   
    
    resp = lambda_handler(event, None)      

    assert resp['statusCode'] == 400  
    assert resp['body'] == 'invalid request url'

def test_lambda_handler_wrong_request_method(dynamodb_table):     
    event = {
        "path": "/user", "httpMethod": "DELETE",    
        "queryStringParameters": {"name": "sample_user_name" }
            }   
    
    resp = lambda_handler(event, None)      

    assert resp['statusCode'] == 400  
    assert resp['body'] == 'invalid request method'    


def test_user_post_handler_success(dynamodb_table):    
    ret = user_post_handler('sample_user')      
    table = dynamodb_table.Table(os.environ["TABLE_NAME"])
    resp = table.scan(ProjectionExpression="UserID, UserName")   

    assert resp['Items'][0]['UserName'] == 'sample_user'   
    assert resp['Count'] == 1  
    assert ret['ResponseMetadata']['HTTPStatusCode'] == 200


def test_user_post_handler_multiple_items(dynamodb_table):
    ret_1 = user_post_handler('sample_user')  
    ret_2 = user_post_handler('sample_user')  

    table = dynamodb_table.Table(os.environ["TABLE_NAME"])
    resp = table.scan(ProjectionExpression="UserID, UserName")   

    assert resp['Count'] == 2
    assert resp['Items'][0]['UserName'] == 'sample_user'  
    assert resp['Items'][1]['UserName'] == 'sample_user'      
    assert ret_1['ResponseMetadata']['HTTPStatusCode'] == 200
    assert ret_2['ResponseMetadata']['HTTPStatusCode'] == 200

def test_user_post_handler_fail(dynamodb_table):    
    with pytest.raises(Exception, match="Type mismatch for key UserName expected: S actual: N"):
        user_post_handler(1234)

def test_user_post_handler_wrong_table_name():
    with mock_dynamodb(), pytest.raises(Exception, match="Requested resource not found"):
            ret = user_post_handler('sample_user')  

def test_get_dynamo_db_resource():
    with mock_dynamodb():
        resource = get_dynamo_db_resource('us-east-1')      
        assert resource == boto3.resource("dynamodb", 'us-east-1')

def test_get_dynamo_db_table():
    with mock_dynamodb():
        db_table = get_dynamodb_table('test_table','us-east-1')   
        resource = boto3.resource("dynamodb", 'us-east-1')   
        table = resource.Table('test_table')        
        assert db_table == table
        

def test_prepare_response_success():
    ret = prepare_response(200,'success')

    assert isinstance(ret, dict)
    assert ret['statusCode'] == 200

def test_extract_event_blank_qs_name(event_object_blank_qs_name):
    qs_validation_success,user_name,request_method,request_path = \
    extract_event(event_object_blank_qs_name)
    
    assert qs_validation_success == False
    assert user_name == ""
    assert request_method == 'POST'
    assert request_path == '/user'


def test_extract_event_no_qs_name(event_object_no_qs_name):
    qs_validation_success,user_name,request_method,request_path = \
    extract_event(event_object_no_qs_name)
    
    assert qs_validation_success == False
    assert user_name == None
    assert request_method == 'POST'
    assert request_path == '/user'

def test_extract_event_success(event_object_all_fields):
    qs_validation_success,user_name,request_method,request_path = \
    extract_event(event_object_all_fields)
    
    assert qs_validation_success == True
    assert user_name == 'dummy_user'
    assert request_method == 'POST'
    assert request_path == '/user'


def test_get_table_region_success():
    assert get_table_region() == "us-east-1"

def test_get_table_name_success():
    assert get_table_name() == "user-table" 

def test_get_table_name_with_no_env_var(monkeypatch):
    monkeypatch.delenv("TABLE_NAME")
    with pytest.raises(KeyError):
        get_table_name()

def test_get_table_region_with_no_env_var(monkeypatch):
    monkeypatch.delenv("REGION")
    with pytest.raises(KeyError):
        get_table_region()

def test_get_table_region_success1():
    assert get_table_region() == "us-east-1" 
