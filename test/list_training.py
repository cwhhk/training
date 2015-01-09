__author__ = 'chenwei'
# -*- coding: utf-8 -*-
d = {'x': 'A', 'y': 'B', 'z': 'C' }
L = ['Hello', 'World', 18, 'Apple', None]
for k, v in d.iteritems():
    print k, '=', v
aa = [s.lower() for s in L if isinstance(s, str)]
print aa