import os
import boto3
import json

sqs = boto3.client("sqs")
rekognition = boto3.client("rekognition")
dynamodb = boto3.client("dynamodb")
sns = boto3.client("sns")

queue_url = os.environ["SQS_QUEUE_URL"]
table_name = os.environ["TABLE_NAME"]
topic_arn = os.environ["TOPIC_ARN"]

# 1 Use Rekognition to detect max of 10 labels with a confidence of 70 percent.


# 2 Write labels to DynamoDB given a table name and item.


# 3 Publish item to SNS
def triggerSNS(message):
    response = sns.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject="Success!",
    )
    print(response)


# 4 Delete message from SQS


def handler(event, context):
    print(event)
    print(type(event))
    try:
        # process message from SQS
        for Record in event.get("Records"):
            receipt_handle = Record.get("receiptHandle")
            for record in json.loads(Record.get("body")).get("Records"):
                bucket_name = record.get("s3").get("bucket").get("name")
                key = record.get("s3").get("object").get("key")

                # call method #1 to generate image label and store as var "labels"

                # code snippet to create dynamodb item from labels
                db_result = []
                json_labels = json.dumps(labels["Labels"])
                db_labels = json.loads(json_labels)
                for label in db_labels:
                    db_result.append(label["Name"])
                db_item = {"image": {"S": key}, "labels": {"S": str(db_result)}}

                # call method #2 to store "db_item" result on DynamoDB

                # call method #3 sending db_result as a string to trigger SNS.

                # call method #4 to delete img from SQS.

    except Exception as e:
        print(e)
        print("Error processing object from bucket.")
        raise e
