import requests
from get_dnac_token import get_dnac_token
from dnac_creds import DNAC_URL
import json

url = f'{DNAC_URL}/dna/intent/api/v1/network-health'

headers = {
    'X-Auth-Token': get_dnac_token(),
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers, verify=False, timeout=5)
print(response.status_code)
print(json.dumps(response.json(), indent=4))