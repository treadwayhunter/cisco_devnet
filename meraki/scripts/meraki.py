#from meraki_info import organizations_url, headers
from meraki_info import api_key
import requests
from requests import Response
import json



class Meraki:
    
    base_uri = 'https://api.meraki.com/api/v1'
    valid_product_types = ['appliance', 'camera', 'cellularGateway', 'sensor', 'switch', 'wireless']

    def __init__(self, api_key):
        self.headers = {
            'Authorization': f'Bearer {api_key}'
        }

    # This is probably not good outside of this test environment
    # but this will get the organization I am attached to that != self
    def get_org(self):
        url = f'{Meraki.base_uri}/organizations'
        response: Response = requests.get(url, headers=self.headers)
        
        #self.json_print(response.json())
        org_id = response.json()[1]['id']
        return org_id

    def get_networks(self, org_id: str):
        url = f'{Meraki.base_uri}/organizations/{org_id}/networks'
        response: Response = requests.get(url, headers=self.headers)
        #self.json_print(response.json())
        networks: list = list(response.json())
        return networks
    
    def create_network(self, org_id: str, name: str, product_types: list[str]):
        if not product_types:
            raise ValueError('product_types cannot be empty!')

        invalid_types = set(product_types) - set(self.valid_product_types)
        if invalid_types:
            raise ValueError(f'Invalid product types: {list(invalid_types)}')

        url = f'{Meraki.base_uri}/organizations/{org_id}/networks'
        data = {
            'name': name,
            'productTypes': product_types
        }
        response: Response = requests.post(url, headers=self.headers, json=data)

        print(response.status_code)
        if response.status_code == 201:
            print(f'{name} successfully created!')
        else:
            print(f'{name} was not created.')
    
    def get_inventory(self, org_id):
        url = f'{Meraki.base_uri}/organizations/{org_id}/inventory/devices'
        response: Response = requests.get(url, headers=self.headers)
        print(response.json())

    # can't do this in the sandbox
    def add_device_to_network(self, org_id, network_id, serial):
        pass

    def json_print(self, data):
        print(json.dumps(data, indent=2))

if __name__ == '__main__':
    meraki = Meraki(api_key)
    org_id = meraki.get_org()
    print(f'Cisco DevNet Test Organization: {org_id}')
    networks = meraki.get_networks(org_id)
    #print(networks)
    network_names = [network['name'] for network in networks]
    print(network_names)
    test_network = 'Test Network'
    if test_network not in network_names:
        # create the network
        product_types = [
            'switch',
            'wireless'
        ]
        meraki.create_network(org_id, test_network, product_types)
    else:
        # don't create the network
        print(f'{test_network} already exists! Skipping this step.')
    meraki.get_inventory(org_id) # inventory is sadly empty