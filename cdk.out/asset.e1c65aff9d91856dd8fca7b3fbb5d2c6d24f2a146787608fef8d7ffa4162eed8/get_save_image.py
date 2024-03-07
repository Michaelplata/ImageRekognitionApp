import os
import json
import boto3
import requests
import botocore.exceptions

s3_client = boto3.client("s3")
S3_BUCKET = os.getenv('BUCKET_NAME')

#1 Create function to download the content from a url without a filename and print any request exception.
def download_image(url):
    try:
        response = requests.get(url)
        return response.content
    except requests.exceptions.RequestException as e:
        print(e)
        return None



#2 Create a function to upload the file to s3 and print any exception.
def upload_image_to_s3(image_data, name):
    try:
        s3_client.put_object(Body=image_data, Bucket=S3_BUCKET, Key=name)
    except botocore.exceptions.ClientError as e:
        print(e)
        return None
    return True

    

def handler(event, context):
    url = event["queryStringParameters"]["url"]
    name = event["queryStringParameters"]["name"]

    # call method #1 to download image
    image_data = download_image(url)

    # call method #2 to upload image to s3
    upload_image_to_s3(image_data, name)


    return {
        'statusCode': 200,
        'body': json.dumps('Successfully Uploaded Img!')
    }
