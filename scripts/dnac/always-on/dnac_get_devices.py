import requests
from dnac_creds import TOKEN_URL, USER, PASSWORD, DEVICES_URL
from dnac_auth_token import get_auth_token

def get_device_list(url, headers):
    response = requests.get(url, headers=headers, verify=False)

    device_list = []
    if response.status_code == 200:
        device_list = response.json()['response']

    return device_list


if __name__ == '__main__':
    token = get_auth_token(TOKEN_URL, USER, PASSWORD)
    headers = {
        'X-Auth-Token': token,
        'Accept': 'application/json'
    }
    devices = get_device_list(DEVICES_URL, headers)
    for device in devices:
        print(f'{device["hostname"]} {device["id"]}')