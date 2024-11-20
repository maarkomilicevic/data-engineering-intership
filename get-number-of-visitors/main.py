import sys
import boto3
import requests
import json

def get_token_from_secret_manager(secret_name, region_name="eu-west-1"):


    secrets_client = boto3.client(
        "secretsmanager",
        region_name=region_name,
        aws_access_key_id=sys.argv[1],
        aws_secret_access_key=sys.argv[2],
        aws_session_token=sys.argv[3]
    )



    response = secrets_client.get_secret_value(SecretId=secret_name)
    return response['SecretString']




token = json.loads(get_token_from_secret_manager("tourist_estimate_token"))
TOKEN = token['tourist_estimate_token']
URL = "https://rq5fbome43vbdgq7xoe7d6wbwa0ngkgr.lambda-url.eu-west-1.on.aws/"
DATE = input('Input date in form YYYY-MM-DD: ')

headers = {
    "Authorization": f"Bearer {TOKEN}"
}
params = {
    "date": DATE
}

response = requests.get(URL, headers=headers, params=params)

if response.status_code == 200:
    print(f'Number of visitors for date: {DATE} is: ')
    for line in response.json()['info']:
        print(line['name'] + ': ' + str(line['estimated_no_people']))
else:
    print(f"Error: {response.status_code}, {response.text}")

