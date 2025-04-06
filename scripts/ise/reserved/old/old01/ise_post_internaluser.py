# This script creates a custom user

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

user = {
    'InternalUser': {
        'name': 'treadwayh',
        'description': 'Created using python Requests library',
        'enabled': True,
        'email': 'testemail@gmail.com',
        'password': 'testpassword',
        'firstName': 'Hunter',
        'lastName': 'Treadway'
    }
}

try:
    response = requests.post(BASE_URL, json=user, auth=HTTPBasicAuth(USER, PASSWORD), headers=HEADERS, verify=False, timeout=10)

    print(f'Status Code: {response.status_code}')



    #users = response.json()
    #print('Configured Users:')
    #print(json.dumps(users, indent=4))

    #with open('internal_users.json', 'w') as file:
    #    json.dump(users, file, indent=4)
except requests.exceptions.RequestException as e:
    print(f'An error has occurred: {e}')