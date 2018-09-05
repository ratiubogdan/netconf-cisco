#! /usr/bin/env python
#
# Connect to the NETCONF server passed on the command line and
# display their capabilities. This script and the following scripts
# all assume that the user calling the script is known by the server
# and that suitable SSH keys are in place. For brevity and clarity
# of the examples, we omit proper exception handling.
#
# $ ./nc01.py broccoli
# if you get the unknown host key error, I just commented out that part.

import sys, warnings
import xml.etree.ElementTree as ET

warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager


# from ncclient.xml_ import new_ele

def demo(host, user, passw):
    m = manager.connect(host=host, port=22, username=user, password=passw, device_params={'name': 'nexus'}, )
    for c in m.server_capabilities:
        print(c)
    # sw_info = new_ele('get-config')
    # print sw_info
    # res = m.rpc(sw_info)
    # print res
    # print m.get_config('running')

    # print m.get_ssh_subsystem_names()
    request = '''
                        <show xmlns="http://www.cisco.com/nxos:1.0">
                            <version>
                            </version>
                        </show>
                       '''
    rec = m.get(('subtree', request)).data_xml
    print(rec)
    print("acuma afisez xml daca pot")
    root = ET.fromstring(rec)
    print("incerc sa afisez elementele")
    print ("root=", root, "tag=", root.tag, "Attrib=", root.attrib)

    host = root.find('.//{http://www.cisco.com/nxos:1.0:sysmgrcli}host_name')
    print("am hostname=", host.text)


    m.close_session()


if __name__ == '__main__':
    demo(sys.argv[1], sys.argv[2], sys.argv[3])
