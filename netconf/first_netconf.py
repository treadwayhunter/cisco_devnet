from ncclient import manager
import xml.dom.minidom as pretty_xml

# 10.10.20.48
# developer
# C1sco12345

with manager.connect(
    host='10.10.20.48',
    port=830,
    username='developer',
    password='C1sco12345',
    hostkey_verify=False
) as m:
    running_config = m.get_config(source="running").data_xml

    parsed_xml = pretty_xml.parseString(running_config)
    print(parsed_xml.toprettyxml(indent='  ')) # 2 space indentation
