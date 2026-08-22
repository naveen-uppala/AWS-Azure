import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentTable')  # <-- replace with your actual table name

def lambda_handler(event, context):
    
    # Read values passed in through the event (test event / trigger payload)
    name = event.get('Name')
    course = event.get('Course')
    
    # Basic validation — good practice to show students
    if not name or not course:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing required fields: Name and Course')
        }
    
    item = {
        'StudentId': str(uuid.uuid4()),
        'Name': name,
        'Course': course,
        'EnrolledOn': str(datetime.now())
    }
    
    table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Data inserted successfully: {item}")
    }
