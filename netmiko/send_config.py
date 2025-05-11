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

config_commands = [
    'interface GigabitEthernet2',
    'description Configured by Netmiko',
    'ip address 192.168.10.1 255.255.255.0'
]

with ConnectHandler(**details) as connection:
    output = connection.send_config_set(config_commands)
    print(output)
    # the output is actually just the typical switch configs
    #cat8000v(config)#interface GigabitEthernet2
    #cat8000v(config-if)#description Configured by Netmiko
    #cat8000v(config-if)#ip address 192.168.10.1 255.255.255.0
    #cat8000v(config-if)#end
    #cat8000v#

    #cat8000v#show run int G2
    #Building configuration...
    #
    #Current configuration : 136 bytes
    #!
    #interface GigabitEthernet2
    # description Configured by Netmiko
    # ip address 192.168.10.1 255.255.255.0
    # shutdown
    # negotiation auto
    #end