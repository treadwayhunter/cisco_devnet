import requests
from requests.auth import HTTPBasicAuth
import json

   # 'host': '10.10.20.48',
   # 'port': 22,
   # 'username': 'developer',
   # 'password': 'C1sco12345'
HOST = '10.10.20.48'
USER = 'developer'
PASSWORD = 'C1sco12345'

URL = f'https://{HOST}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces'

HEADERS = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

with requests.get(URL, headers=HEADERS, auth=HTTPBasicAuth(USER, PASSWORD), verify=False, timeout=5) as response:
    if response.status_code == 200:
        print('Request Successful')
        #print(json.dumps(response.json(), indent=2))
        data = response.json()

        with open('interfaces.json', 'w') as file:
            json.dump(data, file, indent=4)
    else:
        print('Failed to retrieve data')