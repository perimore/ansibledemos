#!/usr/bin/env python
''' Render a template '''

from jinja2 import Template

template = Template("interface {{ intf }}\n shutdown")

for x in [1, 2]:
    print template.render(intf="Ethernet%s" % x)
