import requests
from dnac_creds import TOKEN_URL, USER, PASSWORD, DEVICES_URL
from dnac_auth_token import get_auth_token

token = get_auth_token(TOKEN_URL, USER, PASSWORD)
headers = {
    'X-Auth-Token': token,
    'Accept': 'application/json'
}


response = requests.get(DEVICES_URL, headers=headers, verify=False)

device_list = []
if response.status_code == 200:
    device_list = response.json()['response']

for device in device_list:
    print(device['hostname'])