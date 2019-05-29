from io import StringIO 
import json

data_file = open("matiari_2", "r")
dumping=json.load(data_file)
v = dumping[0]['data']['weather']

for value in v:
    print(v[0]['hourly']['tempC'])

'''import json
from pprint import pprint
'''
'''with open('matiari_5.json','r') as fh:
    json_str= fh.read()
    json_value=json.loads(json_str)
    print(type(json_value))
'''
