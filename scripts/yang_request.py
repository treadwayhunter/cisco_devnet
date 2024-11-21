import requests
from requests.auth import HTTPBasicAuth
import json

HOST = '10.10.20.48'
USER = 'developer'
PASSWORD = 'C1sco12345'

URL = f'https://{HOST}/restconf/data/ietf-yang-library:modules-state'

HEADERS = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

try:
    print('Trying to reach')
    response = requests.get(url=URL, headers=HEADERS, auth=HTTPBasicAuth(USER, PASSWORD), timeout=5, verify=False)

    if response.status_code == 200:
        #print(response.json())
        data = response.json()
        with open('yang_model.json', 'w') as file:
            json.dump(data, file, indent=4)
    else:
        print('bad response')
except:
    print('woops')