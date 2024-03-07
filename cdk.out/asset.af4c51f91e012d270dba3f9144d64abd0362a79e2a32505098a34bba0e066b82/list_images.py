import os
import boto3
import json

table_name = os.environ["TABLE_NAME"]

#1 create Function to scan and list all items from a DynamoDB table.

def handler(event, context):
    # call method #1 to scan items from DynamoDB and put them in a variable named response.

    return {
        "body": json.dumps(response),
        "statusCode": 200
    }
