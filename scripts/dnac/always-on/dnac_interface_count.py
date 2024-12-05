import requests
from dnac_creds import INTERFACE_URL, TOKEN_URL, USER, PASSWORD
from dnac_auth_token import get_auth_token
import json

def get_interface_count(url, headers):
    response = requests.get(url, headers=headers, verify=False, timeout=10)

    #print(response.status_code)
    print(json.dumps(response.json(), indent=4))

if __name__ == '__main__':
    token = get_auth_token(TOKEN_URL, USER, PASSWORD)
    headers = {
        'X-Auth-Token': token,
        'Accept': 'application/json'
    }
    get_interface_count(INTERFACE_URL, headers)