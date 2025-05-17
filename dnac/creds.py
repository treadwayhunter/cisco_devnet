import requests
from requests.auth import HTTPBasicAuth

# reservable
_username = 'administrator'
_password = 'Cisco1234!'
_ADDRESS = '10.10.20.85'
_TOKEN_PATH = 'https://' + _ADDRESS + '/dna/system/api/v1/auth/token'

def get_reservable_creds():
    return _username, _password

def get_auth_token():
    token = ''
    try:
        response = requests.post(_TOKEN_PATH, auth=HTTPBasicAuth(_username, _password), verify=False)

        if response.status_code == 200:
            token = response.json()['Token']
    except Exception as e:
        print('AN ERROR OCCURRED:', e)

    return token

if __name__ == '__main__':
    token = get_auth_token()
    print(token)