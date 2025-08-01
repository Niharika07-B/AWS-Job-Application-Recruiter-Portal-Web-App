import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    table_name = 'YOUR-TABLE-NAME'
    response = dynamodb.scan(TableName=table_name)
    items = response.get('Items', [])

    # Convert DynamoDB items to plain dicts
    applications = []
    for item in items:
        applications.append({
            'id': item.get('id', {}).get('S', ''),
            'name': item.get('name', {}).get('S', ''),
            'email': item.get('email', {}).get('S', ''),
            'phone': item.get('phone', {}).get('S', ''),
            'position': item.get('position', {}).get('S', ''),
            'resume_url': item.get('resume_url', {}).get('S', ''),
        })

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'applications': applications})
    }
