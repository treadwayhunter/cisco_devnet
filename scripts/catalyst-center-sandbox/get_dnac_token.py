import requests
from requests.auth import HTTPBasicAuth
from dnac_creds import DNAC_URL, TOKEN_ENDPOINT, USER, PASSWORD, TOKEN_FILE
import json
from datetime import datetime

TOKEN = 'token'
DATETIME = 'datetime'

# return an integer of the last time since minutes
def time_diff(time1, time2):
    diff = time2 - time1 # timedelta obj
    minutes = int(diff.total_seconds() / 60)
    print(f'TIME SINCE LAST TOKEN: {minutes}')
    return minutes


# instead of getting the token each time, know the token is good for an hour.
# create a file that contains the token and the time it was retrieved
    # if the file doesn't exist, get a new token and place it in the file, and return the token
    # if the file does exist, check the datetime field
        # if the datetime is over an hour ago, get a new token, place it in the token field, and return the token
        # if the datetime is valid, retrieve the token, and return this token without making a new request
def get_dnac_token():
    url = f'{DNAC_URL}{TOKEN_ENDPOINT}'
    user = USER
    password = PASSWORD
    timeout = 5
    print('Getting token...')
    try:
        print('Attempting to get token from file')
        with open(TOKEN_FILE, 'r') as file:
            data = json.load(file)

        #print(data)
        time_now = datetime.now()
        time_old = datetime.fromisoformat(data[DATETIME])
        minutes = time_diff(time_old, time_now)
        if minutes < 50:
            token = data[TOKEN]        
            return token
        else:
            print('Token has expired, or is about to expire.')

    except:
        print(f'File does not exist: {TOKEN_FILE}')
        pass

    try:
        print('Attempting to get token from request')
        response = requests.post(url, auth=HTTPBasicAuth(user, password), verify=False, timeout=timeout)
        if response.status_code != 200:
            raise Exception(f'Error {response.status_code}: Invalid Credentials')
        
        token = response.json()['Token']
        time = datetime.now()
        data = {
            TOKEN: token,
            DATETIME: time.isoformat()
        }

        with open(TOKEN_FILE, 'w') as file:
            json.dump(fp=file, obj=data, indent=4)

        return token
    except:
        print('Error getting token')



if __name__ == '__main__':
    url = f'{DNAC_URL}{TOKEN_ENDPOINT}'
    print(get_dnac_token())

