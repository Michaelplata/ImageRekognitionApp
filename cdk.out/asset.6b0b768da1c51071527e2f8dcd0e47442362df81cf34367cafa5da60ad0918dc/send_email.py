from xml.etree.ElementTree import Element, ElementTree, tostring
import requests
import boto3


def get_thirdparty_endpoint():
    '''
    Get thirdparty endpoint from SSM Parameter Store
    '''
    ssm_client = boto3.client('ssm', region_name='us-east-1')
    response = ssm_client.get_parameter(
        Name='thirdparty_endpoint', WithDecryption=False)
    return response['Parameter']['Value']

#1 Convert JSON data to XML string


#2 Send XML string with HTTP POST


def handler(event, context):

    # call method #1 with var "event" to convert json to xml

    # call method #2 to post xml

    return {
        'statusCode': 200,
        "message": "Success!"
    }
