# -*- coding: utf-8 -*-
# python

# python nested dictionary/list to JSON

#En este script se pasa de un objeto en python y se transforma 
#En JSON

import json

python_object = ['x3', {'x4': ('8', None, 1.0, 2)}]

print json.dumps(python_object)
# ["x3", {"x4": ["8", null, 1.0, 2]}]