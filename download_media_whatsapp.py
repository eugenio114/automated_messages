import os
import urllib.request
from twilio.rest import Client
import boto3

# Twilio API credentials
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

# S3 credentials
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
bucket_name = 'YOUR_BUCKET_NAME'

# Set up Twilio API client
twilio_client = Client(account_sid, auth_token)

# Get all media messages sent to the WhatsApp chat
media_messages = twilio_client.messages.list(media_content_type=['image/jpeg', 'image/png', 'video/mp4'], to='whatsapp:+14155238886')

# Set up S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Download media files and upload them to S3 bucket
for media in media_messages:
    media_url = media.media_url
    media_type = media.content_type.split('/')[0]
    filename = os.path.basename(media_url)
    local_filepath = f'{media_type}/{filename}' # Create subdirectory for each media type
    urllib.request.urlretrieve(media_url, local_filepath)
    s3.upload_file(local_filepath, bucket_name, f'{media_type}/{filename}')
    os.remove(local_filepath)
    print(f'Uploaded {filename} to S3 bucket {bucket_name}')
