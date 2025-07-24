import json
import boto3
import base64
import uuid

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Parse the incoming data
    if 'body' in event:
        if isinstance(event['body'], str):
            data = json.loads(event['body'])
        else:
            data = event['body']
    else:
        # If 'body' is not present, treat event as the data itself (for direct Lambda testing)
        data = event

    name = data.get('name', '')
    email = data.get('email', '')
    phone = data.get('phone', '')
    position = data.get('position', '')
    coverletter = data.get('coverletter', '')
    resume_b64 = data.get('resume', '')
    resume_filename = data.get('resumefilename', 'resume.pdf')
    resume_type = data.get('resumetype', 'application/pdf')

    # Decode the base64 encoded resume
    resume_data = base64.b64decode(resume_b64)

    # Upload the resume to the S3 bucket
    bucket_name = 'YOUR-BUCKET-NAME'  # Change this to your S3 bucket name
    unique_id = str(uuid.uuid4())
    s3_key = f"resumes/{unique_id}_{resume_filename}"
    s3.put_object(Body=resume_data, Bucket=bucket_name, Key=s3_key, ContentType=resume_type)

    # Add the data to the DynamoDB table
    table_name = 'YOUR-TABLE-NAME'
    dynamodb.put_item(
        TableName=table_name,
        Item={
            'id': {'S': unique_id},
            'name': {'S': name},
            'email': {'S': email},
            'phone': {'S': phone},
            'position': {'S': position},
            'coverletter': {'S': coverletter},
            'resume_url': {'S': f's3://{bucket_name}/{s3_key}'}
        }
    )

    # Return a response
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': 'Application submitted successfully'})
    }

    return response
