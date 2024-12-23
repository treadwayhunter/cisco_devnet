# This script creates ISE endpoints
# MAC Addresses were generated randomly and placed into a set to ensure no duplicates
# Then, for each MAC Address, a POST request was generated to send the 'device' to ISE
# This was actually slow and cumbsersome. There is likely a way to perform bulk requests with API
# Even if there isn't a way to do bulk requests, ISE has a 'import csv' function

import requests
from requests.auth import HTTPBasicAuth
import json
import random

hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def mac_gen():
    mac = ''
    for i in range(12):
        if i % 2 == 0 and i != 0:
            mac += ':'
        mac += hex_list[random.randint(0, 11)]
    return mac


mac_set = { mac_gen() for i in range(1000) } # this generates a set of mac addresses, ensures no duplicates
mac_list = list(mac_set) # changed to list for easy access. I still don't want duplicates, so that's why I still have a set

HOST = '10.10.20.77'
USER = 'admin'
PASSWORD = 'QAWSedrf1234!'
API_ENDPOINT = 'ers/config/endpoint'

URL = f'https://{HOST}/{API_ENDPOINT}'

HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

try:
    for mac in mac_list:
        endpoint = {
            'ERSEndPoint': {
                'name': mac,
                'description': 'My Endpoint',
                'mac': mac,
            }
        }

        response = requests.post(url=URL, json=endpoint, auth=HTTPBasicAuth(USER, PASSWORD), verify=False, timeout=10, headers=HEADERS)

        #print(response.status_code)
        if response.status_code == 201:
            print(f'{mac} added!')
        else:
            print(f'{mac} got a response code other than 201')

except:
    print('There was an error!')