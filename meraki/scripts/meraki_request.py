# This module uses the requests library for making requests
# to the API endpoint

import requests
from requests import Response
import json
from meraki_info import organizations_url, headers

def print_status_code(code):
    print(f'Response Status: {code}')

def print_response_data(response: Response):
    if response.ok:
        data = response.json()
        print(json.dumps(data, indent=4))

print('GET ORGANIZATION')
print('**************************************')
response: Response = requests.get(organizations_url, headers=headers)
print_status_code(response.status_code)
print_response_data(response)

org_id = response.json()[1]['id']
print(f'Org Id: {org_id}')
print('**************************************')

# GET /organizations/{organizationId}/networks
print('GET NETWORKS')
print('**************************************')
response: Response = requests.get(f'{organizations_url}/{org_id}/networks', headers=headers)
print_status_code(response.status_code)
print_response_data(response)
print('**************************************')


# POST /organizations/{organizationId}/networks

print('CREATE NETWORKS')
print('**************************************')
data = {
    'name': 'test_network',
    'productTypes': [
        'switch',
        'wireless'
    ]
}
response: Response = requests.post(f'{organizations_url}/{org_id}/networks', json=data, headers=headers)
print_status_code(response.status_code)
print_response_data(response)
print('**************************************')
