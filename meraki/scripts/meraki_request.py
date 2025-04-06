# This module uses the requests library for making requests
# to the API endpoint

import requests
import json
from meraki_info import organizations_url, headers


response = requests.get(organizations_url, headers=headers)

data = response.json()

print(json.dumps(data, indent=4))