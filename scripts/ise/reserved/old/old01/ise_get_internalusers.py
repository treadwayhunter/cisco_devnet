# This gets a list of internal users from ISE

import requests
from requests.auth import HTTPBasicAuth
import json

HOST = '10.10.20.77'
USER = 'admin'
PASSWORD = 'QAWSedrf1234!'
ENDPOINT = 'ers/config/internaluser'

BASE_URL = f'https://{HOST}/{ENDPOINT}'

HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

try:
    response = requests.get(BASE_URL, auth=HTTPBasicAuth(USER, PASSWORD), headers=HEADERS, verify=False, timeout=10)

    print(f'Status Code: {response.status_code}')
    #print(f'Response Text: {response.text}')
    #response.raise_for_status()

    users = response.json()
    print('Configured Users:')
    print(json.dumps(users, indent=4))

    with open('internal_users.json', 'w') as file:
        json.dump(users, file, indent=4)
except requests.exceptions.RequestException as e:
    print(f'An error has occurred: {e}')