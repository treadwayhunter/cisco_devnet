from ncclient import manager
import xml.dom.minidom as pretty_xml

# 10.10.20.48
# developer
# C1sco12345

interface_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>

"""

with manager.connect(
    host='10.10.20.48',
    port=830,
    username='developer',
    password='C1sco12345',
    hostkey_verify=False
) as m:
    running_config = m.get_config(source="running", filter=interface_filter).data_xml

    parsed_xml = pretty_xml.parseString(running_config)
    print(parsed_xml.toprettyxml(indent='  '))  # Pretty-print with 2-space indentation
