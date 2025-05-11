from ncclient import manager
import xml.dom.minidom as pretty_xml
from getpass import getpass

# 10.10.20.48
# developer
# C1sco12345
pwd = getpass('Password: ')
details = {
    'host': '10.10.20.48',
    'port': 830,
    'username': 'developer',
    'password': pwd,
    'hostkey_verify': False
}

with manager.connect(**details) as m:
    running_config = m.get_config(source="running").data_xml

    parsed_xml = pretty_xml.parseString(running_config)
    print(parsed_xml.toprettyxml(indent='  ')) # 2 space indentation
