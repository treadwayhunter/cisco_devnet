import requests
from requests.auth import HTTPBasicAuth
from ise_configs import ERS_USER, ERS_PASS, HOST
import json

# return a list of resources
# the endpoint for internalusers is paginated, only returns a select amount.
# This function runs recursively, running until every page of resources has been added to the list
def get_internalusers(url, user, password):


    resource_list = []

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    try:
        response = requests.get(url, auth=HTTPBasicAuth(user, password), headers=headers, verify=False, timeout=5)
        print(response.status_code)
        if response.status_code != 200: # in case a page is not gotten in the recursive call, this should be editted.
            print(f'Something is broke: {url}')
            return []

        search_result = response.json()['SearchResult']
        endpoints = search_result['resources']

        print(search_result['nextPage'])

        resource_list = [*endpoints]

        # make recursive calls for each page
        if 'nextPage' in search_result:
            href = search_result['nextPage']['href']
            resource_list = [*resource_list, *get_internalusers(href, user, password)]

    except Exception as e:
        print(f'{e}')

    return resource_list

if __name__ == '__main__':
    endpoint = 'ers/config/internaluser?size=100&page=1'
    url = f'{HOST}/{endpoint}'
    print(get_internalusers(url, ERS_USER, ERS_PASS))