#! /usr/bin/env python

import path_macrotemplate as pmt

template = '${lastname}; ${prename}'

values = {'prename': 'Wolfgang Amadeus', 'lastname': 'Mozart'}

t = pmt.Template(template)
f = pmt.Functions(values)
out = t.substitute(values, f.functions)

print(out)
