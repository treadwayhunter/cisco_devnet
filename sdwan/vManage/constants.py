import requests
import json


IP_ADDRESS = '10.10.20.90'
USERNAME = 'admin'
PASSWORD = 'C1sco12345'

def json_print(obj: str):
    print(json.dumps(obj, indent=4))