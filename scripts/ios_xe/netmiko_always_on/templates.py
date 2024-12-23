from netmiko import ConnectHandler
from getpass import getpass # a safe to get password inputs from users
import json

device_info = {
    'device_type': 'cisco_xe',
    'host': 'devnetsandboxiosxe.cisco.com',
    'username': 'admin',
}

device_info['password'] = getpass(f'Input Password for {device_info["host"]}: ')

with ConnectHandler(**device_info, ) as connection:
    output = connection.send_command('show ip int bri', use_textfsm=True)

print(json.dumps(output, indent=4))

# Now that I have the output, I can go and send changes to the interfaces based on the results
# show ip int brief doesn't seem to work here, but it may in other lab environments.
# show interfaces works fine, and gives me the description like I like, but maybe too much information otherwise.

# I could quickly interact with thousands of interfaces rapidly.
# Keep in mind special interfaces and devices