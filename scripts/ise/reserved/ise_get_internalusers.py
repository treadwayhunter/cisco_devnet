import requests
from requests.auth import HTTPBasicAuth
from ise_configs import ERS_USER, ERS_PASS, HOST
import json

# return a list of resources
def get_internalusers(url, user, password):


    resource_list = []

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    try:
        response = requests.get(url, auth=HTTPBasicAuth(user, password), headers=headers, verify=False, timeout=5)
        print(response.status_code)
        if response.status_code != 200:
            print('Something is broke')
            return []

        #print(json.dumps(response.json(), indent=4))
        # make recursive calls to get all
        search_result = response.json()['SearchResult']
        endpoints = search_result['resources']

        print(search_result['nextPage'])

        resource_list = [*endpoints]

        if 'nextPage' in search_result:
            print('There is a next page')
            href = search_result['nextPage']['href']
            resource_list = [*resource_list, *get_internalusers(href, user, password)]



        #print(json.dumps(endpoints, indent=4))

    except Exception as e:
        print(f'{e}')

    return resource_list

if __name__ == '__main__':
    endpoint = 'ers/config/internaluser?size=100&page=1'
    url = f'{HOST}/{endpoint}'
    print(get_internalusers(url, ERS_USER, ERS_PASS))