from netmiko import ConnectHandler

# had to be connected to devnet vpn to access this device
details = {
    'device_type': 'cisco_xe',
    'host': '10.10.20.48',
    'port': 22,
    'username': 'developer',
    'password': 'C1sco12345'
}


with ConnectHandler(**details) as connection:
    output = connection.send_command('show run int lo0')

print(output)

