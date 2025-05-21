import requests
from constants import USERNAME, PASSWORD, json_print
from authentication import Authentication
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Inventory:
    def __init__(self, base_url, token, jsessionid):
        self.base_url = base_url
        self.token = token
        self.jsessionid = jsessionid
        self.inventory = []

    def get_inventory(self, print_result=False):
        api = '/dataservice/device'
        url = self.base_url + api
        print(self.token)
        print(self.jsessionid)
        headers = {
            'X-XSRF-TOKEN': self.token,
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers, cookies=self.jsessionid, verify=False)
        if response:
            #print(response.status_code)
            if print_result:
                json_print(response.json())
            self.inventory = response.json().get("data", [])
        else:
            print('No response')
            self.inventory = []

    def print_inventory(self):
        if self.inventory:
            print(f"{'Hostname':20} {'Model':20} {'System IP':15} {'Reachability':15} {'Site Name':20} {'Version':15}")
            print("-" * 110)
            for device in self.inventory:
                print(f"{device['host-name'][:20]:20} "
                      f"{device['device-model'][:20]:20} " 
                      f"{device['system-ip'][:15]:15} "
                      f"{device['reachability'][:15]:15} "
                      f"{device['site-name'][:20]:20} "
                      f"{device['version'][:15]:15}")


        else:
            print('No inventory has been gathered...')
            print('Try running get_inventory() first')

if __name__ == '__main__':
    base_url = 'https://10.10.20.90'
    print('inventory.py')
    Auth = Authentication(base_url)
    jsessionid = Auth.get_jsessionid(USERNAME, PASSWORD)
    #print(jsessionid)
    token = Auth.get_token(jsessionid)
    #print(token)
    inventory = Inventory(base_url, token, jsessionid)
    inventory.get_inventory()
    inventory.print_inventory()
    



