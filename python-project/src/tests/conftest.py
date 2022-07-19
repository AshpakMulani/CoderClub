# conftest.py

from modulefinder import Module
import pytest
from moto import mock_dynamodb
import boto3
import os

@pytest.fixture(autouse=True)
def env_set(monkeypatch):
    monkeypatch.setenv('TABLE_NAME', 'user-table')
    monkeypatch.setenv('REGION', 'us-east-1') 


@pytest.fixture
def event_object_all_fields():
    return{
        "body": "eyJ0ZXN0IjoiYm9keSJ9",
        "resource": "/{proxy+}",
        "path": "/user",
        "httpMethod": "POST",
        "isBase64Encoded": True,
        "queryStringParameters": {
                "name": "dummy_user"
        },
        "multiValueQueryStringParameters": {
            "name": [
                    "dummy_user"
            ]
        }
    }


@pytest.fixture
def event_object_no_qs_name():
    return{
        "body": "eyJ0ZXN0IjoiYm9keSJ9",
        "resource": "/{proxy+}",
        "path": "/user",
        "httpMethod": "POST",
        "isBase64Encoded": True,
        "queryStringParameters": {
        },
        "multiValueQueryStringParameters": {
        }
    }

@pytest.fixture
def event_object_blank_qs_name():
    return{
        "body": "eyJ0ZXN0IjoiYm9keSJ9",
        "resource": "/{proxy+}",
        "path": "/user",
        "httpMethod": "POST",
        "isBase64Encoded": True,
        "queryStringParameters": {
                "name": ""
        },
        "multiValueQueryStringParameters": {
            "name": [
                    ""
            ]
        }
    }


@pytest.fixture
def dynamodb_table():    
    with mock_dynamodb():
        resource = boto3.resource('dynamodb','us-east-1')
        resource.create_table(
            TableName=os.environ["TABLE_NAME"],
            AttributeDefinitions=[
                {'AttributeName': 'UserID', 'AttributeType': 'S'},
                {'AttributeName': 'UserName', 'AttributeType': 'S'}
            ],            
            KeySchema=[
                {'AttributeName': 'UserID', 'KeyType': 'HASH'},
                {'AttributeName': 'UserName', 'KeyType': 'RANGE'}
                ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5,
            }
        )        
        yield resource
        