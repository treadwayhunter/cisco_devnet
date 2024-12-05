import requests
from requests.auth import HTTPBasicAuth
from dnac_creds import TOKEN_URL, USER, PASSWORD


# get a token first, then make repeated requests using the token
# The token is valid for 1 hour
def get_auth_token(url, user, password):
    token = ''
    try:
        response = requests.post(url, auth=HTTPBasicAuth(user, password), verify=False)

        if response.status_code == 200:
            token = response.json()['Token']
    except:
        print('AN ERROR OCCURRED')

    return token

if __name__ == '__main__':
    token = get_auth_token(TOKEN_URL, USER, PASSWORD)
    print(token)