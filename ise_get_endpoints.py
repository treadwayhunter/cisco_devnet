import requests
from requests.auth import HTTPBasicAuth
import json

HOST = '10.10.20.77'
USER = 'admin'
PASSWORD = 'QAWSedrf1234!'
API_ENDPOINT = 'ers/config/endpoint'

CERT_PATH = 'PythonRestCert.pem'

BASE_URL = f'https://{HOST}/{API_ENDPOINT}'

HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

try:
    response = requests.get(BASE_URL, auth=HTTPBasicAuth(USER, PASSWORD), headers=HEADERS, verify=False, timeout=10)

    print(f'Status Code: {response.status_code}')

    endpoints = response.json()
    print(json.dumps(endpoints, indent=4))

    with open('endpoints.json', 'w') as file:
        json.dump(endpoints, file, indent=4)

except requests.exceptions.RequestException as e:
    print(f'An error has occurred: {e}')