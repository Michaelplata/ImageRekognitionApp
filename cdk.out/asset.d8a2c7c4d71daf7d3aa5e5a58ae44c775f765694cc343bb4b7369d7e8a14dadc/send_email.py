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
def json_to_xml(event):


#2 Send XML string with HTTP POST
def post_xml(xml_string):
    endpoint = get_thirdparty_endpoint()
    headers = {'Content-Type': 'application/xml'}
    response = requests.post(endpoint, data=xml_string, headers=headers)
    return response.status_code, response.text
    # return response.status_code, response.text, response.headers
    # return response.status_code, response.text, response.headers, response.cookies
    # return response.status_code, response.text, response.headers, response.cookies, response.elapsed, response.request, response.history
    # return response.status_code, response.text, response.headers, response.cookies, response.elapsed, response.request, response.history, response.raw, response.url, response.history, response.request, response.history, response.request, response.history, response.request, response.history, response.request, response.history, response.request, response.history, response.request, response.history, response.request, response.history, response.request, response.history, response.request, response.history,


def handler(event, context):

    # call method #1 with var "event" to convert json to xml
    xml_string = json_to_xml(event)

    # call method #2 to post xml
    status_code, response_text = post_xml(xml_string)

    # print status code

    return {
        'statusCode': 200,
        "message": "Success!"
    }
