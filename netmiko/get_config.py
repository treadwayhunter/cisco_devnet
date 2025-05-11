# Netmiko test using Cisco DevNet SandBox
# Cisco 8000v switch, 10.10.20.48
# developer/C1sco12345

from netmiko import ConnectHandler


details = {
    'device_type': 'cisco_xe',
    'host': '10.10.20.48',
    'username': 'developer',
    'password': 'C1sco12345'
}

with ConnectHandler(**details) as connection:
    result = connection.send_command('show ip int bri')

print(result)