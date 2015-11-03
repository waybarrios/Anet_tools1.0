# -*- coding: utf-8 -*-
# python

# convert JSON to Python nested dictionary/list

import json

json_data = '["x3", {"x4": ["8", null, 1.0, 2]}]'

python_obj = json.loads(json_data)

print python_obj
# [u'x3', {u'x4': [u'8', None, 1.0, 2]}]