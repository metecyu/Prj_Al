import json
import requests

config = {}
with open('../config.json') as cfg:
  config = json.load(cfg)

url = 'http://%s/todo/api/tasks/2016-05-09' % config['host']
# http://%s:%s/todo/api/v1.0/tasks' % (config['host'], config['port']
print url
resp = requests.get(url)
print resp.text

json_data=json.loads(resp.text)
print json_data