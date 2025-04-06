import meraki
from meraki_info import api_key
import json

print('ORGANIZATIONS')
print('----------------------------------------')
dashboard = meraki.DashboardAPI(api_key, suppress_logging=True)
response = dashboard.organizations.getOrganizations()
print(json.dumps(response, indent=4))
print('----------------------------------------')

print('NETWORKS')
print('----------------------------------------')
response = dashboard.organizations.getOrganizationNetworks('669910444571365342')
print(json.dumps(response, indent=4))
print('----------------------------------------')

