#!/usr/bin/env python
''' Report network device OS version '''

from jinja2 import Template
from netmiko import ConnectHandler
from pprint import pprint
import json

host = 'spine1'

node = {
        'device_type': 'arista_eos',
        'ip': host,
        'username': 'admin',
        'password': '',
        'verbose': False,
}
net_connect = ConnectHandler(**node)

# For human consumption
version_info = net_connect.send_command('show version')
print version_info

# For script consumption
output = net_connect.send_command('show version |json')
version_info = json.loads(output)
print "\n----- JSON structured data -----\n"
pprint(version_info)

#Define the template (Normally loaded from a seperate file)
#http://jinja.pocoo.org/docs/2.9/api/#basics
template = Template("Device {{ host }}\n {{ model  }} running EOS {{ version }}")

# Render the template
print "\n----- Report -----\n"
print template.render(host=host,
                      model=version_info['modelName'],
                      version=version_info['version']
                      )
