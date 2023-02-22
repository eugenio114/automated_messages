import json
import boto3
from twilio.rest import Client

# Set up the Twilio client
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = Client(account_sid, auth_token)

# Define the Lambda function
def lambda_handler(event, context):
    # Get the S3 bucket and object key from the event
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Send a WhatsApp message with Twilio
    message = client.messages.create(
        body='A new file was added to the S3 bucket',
        from_='whatsapp:+14155238886',
        to='whatsapp:+WHATSAPP_NUMBER'
    )
    
    # Print the message SID for reference
    print(message.sid)
