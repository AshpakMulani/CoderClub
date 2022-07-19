import json
import os
import boto3
import uuid
from botocore.exceptions import ClientError
import functools


def get_table_name():
    """
    Read and return DynamoDB table name from environment variable

    Returns
    -------
    string
        DynamoDB table name stored in environment variable 'TABLE_NAME'
    """
    ret_val = os.environ["TABLE_NAME"]
    return ret_val

def get_table_region():
    """
    Read and return DynamoDB table region from environment variable

    Returns
    -------
    string
        DynamoDB table region stored in environment variable 'REGION'
    """
    ret_val = os.environ["REGION"]
    return ret_val

def extract_event(event):
    """
    Extracts and validates fields from event object passed by API endpoint
    
    This function simply returns extracted values as list with first item
    as validation success as true or false

    Parameters
    ----------
    event : dict
        event object passed from AWS API gateway endpoint 

    Returns
    -------
    list
        extracted values from event with first item validation
        success as true or false
    """    
    qs_validation_success = True

    # notice use of .get methind on dict rather than directly accessing key 'name'. 
    # get() method provides a way to return even if key does not exist in dict.
    user_name = event['queryStringParameters'].get('name')
    if user_name is None  or len(str(user_name)) < 1:
        qs_validation_success = False        

    request_method = event['httpMethod']
    request_path= event['path']

    return  [qs_validation_success,user_name,request_method,request_path]
        
def prepare_response(status_code,body):
    """
    Generate response object to return from API endpoint
    
    Parameters
    ----------
    event : dict
        event object passed from AWS API gateway endpoint 

    Returns
    -------
    list
        extracted values from event with first item validation
        success as true or false
    """
    response_object = {}    
    response_object['statusCode'] = status_code
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = body

    return response_object

def lambda_handler(event, context):
    """
    Function handles API endpoint requests
    
    Parameters
    ----------
    event : dict
        event object passed from AWS API gateway endpoint 
    context : dict
        object passed to lambda by default on invocation

    Returns
    -------
    dict
        lambda execution details
    """
    response_object = {}

    # Extracts required details from event object.
    # Remember structure of event object stored in apigateway-aws-proxy.json
    qs_validation_success,user_name,request_method,request_path =  extract_event(event)

    # check for POST operation on user endpoint with query string validation
    if request_path != "/user": # new
        response_object = prepare_response(400, 'invalid request url')
        return response_object
    
    if not qs_validation_success:   # new
        response_object = prepare_response(400, 'invalid query arguments')
        return response_object

            
    if request_method == 'POST':
        post_handler_return = user_post_handler(user_name)
        response_object = prepare_response(
                post_handler_return['ResponseMetadata']['HTTPStatusCode'],
                'user added successfully' if \
                post_handler_return['ResponseMetadata']['HTTPStatusCode']==200 \
                else 'error occured while adding user'
            )
    else:
        response_object = prepare_response(400, 'invalid request method')
        
   
    return response_object    
    


@functools.lru_cache(1)
def get_dynamo_db_resource(region_name):
    return boto3.resource("dynamodb", region_name=region_name)

@functools.lru_cache(1)
def get_dynamodb_table(table_name,table_region):
    dynamodb = get_dynamo_db_resource(table_region)
    table = dynamodb.Table(table_name)
    return table


def user_post_handler(user_name):
    """
    POST request handler for 'user' API endpoint
    
    Parameters
    ----------
    user_name : string
        name passed in query string during POST operation

    Returns
    -------
    list
        extracted values from event with first item validation
        success as true or false
    """    
    table_region = get_table_region()
    table_name= get_table_name()

    # create dynamodb table object
    ddb_table = get_dynamodb_table(table_name, table_region) 

    # prepare dict to insert into DynamoDB table 
    insert_item = {
        'UserID': str(uuid.uuid1()),
        'UserName' : user_name
    }

    try:
        ddb_response = ddb_table.put_item(
            TableName=table_name,
            Item=insert_item
        )
    except ClientError as e:
        raise e               
        #TODO better error handling

    # returning responce from dynamoDB put_item operation
    return ddb_response