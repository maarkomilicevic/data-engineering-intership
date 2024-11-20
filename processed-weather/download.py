import sys

import boto3
import os

import sys

# AWS S3 konfiguracija
AWS_ACCESS_KEY = sys.argv[1]
AWS_SECRET_KEY = sys.argv[2]
AWS_SESSION_TOKEN = sys.argv[3]
BUCKET_NAME = "destination-bucket-mm"
S3_PREFIX = "weather/38348 - Weg zonder naam, Amsterdam, Netherlands/"

# Kreiraj boto3 klijent za S3
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    aws_session_token=AWS_SESSION_TOKEN
)

def download_s3_files(bucket_name, prefix):

    local_directory = os.path.join(os.getcwd(), 'downloaded_files')
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)


    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    for obj in response.get('Contents', []):
        file_key = obj['Key']
        if file_key:
            local_file_path = os.path.join(local_directory, file_key.split('/')[-1])
            s3_client.download_file(bucket_name, file_key, local_file_path)
            print(f"Downloaded: {local_file_path}")





download_s3_files(BUCKET_NAME, S3_PREFIX)



