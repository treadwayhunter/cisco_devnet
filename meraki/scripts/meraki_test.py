import meraki
from meraki_info import api_key
import json

print('GET ORGANIZATIONS')
print('----------------------------------------')
dashboard = meraki.DashboardAPI(api_key, suppress_logging=True)
response = dashboard.organizations.getOrganizations()
print(json.dumps(response, indent=4))
print('----------------------------------------')

org_id = response[1]['id']
print(f'Organizational Network ID == {org_id}')



# GET /organizations/{organizationId}/networks
print('GET NETWORKS')
print('----------------------------------------')
response = dashboard.organizations.getOrganizationNetworks(org_id)
print(json.dumps(response, indent=4))
print('----------------------------------------')

print('SET NETWORKS')
print('----------------------------------------')

