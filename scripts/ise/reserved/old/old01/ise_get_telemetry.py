import requests
from requests.auth import HTTPBasicAuth
import json

HOST = '10.10.20.77'
USER = 'admin'
PASSWORD = 'QAWSedrf1234!'
ENDPOINT = 'ers/config/telemetryinfo'

BASE_URL = f'https://{HOST}/{ENDPOINT}'

HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

try:
    response = requests.get(BASE_URL, auth=HTTPBasicAuth(USER, PASSWORD), headers=HEADERS, verify=False, timeout=10)

    print(f'Status Code: {response.status_code}')

    telemetry = response.json()
    print(json.dumps(telemetry, indent=2))

except requests.exceptions.RequestException as e:
    print(f'An error has occurred: {e}')