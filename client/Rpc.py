
#coding=utf-8

import json
import requests


config = {}
with open('../config.json') as cfg:
  config = json.load(cfg)

# url = 'http://%s:%s/todo/api/tasks/2016-05-09' % (config['host'],config['port'])
# # http://%s:%s/todo/api/v1.0/tasks' % (config['host'], config['port']
# print url
# resp = requests.get(url)
# print resp.text

# json_data=json.loads(resp.text)
# print json_data

def getJson(urlParam):

    url = 'http://%s:%s/%s' % (config['host'],config['port'],urlParam)
    # http://%s:%s/todo/api/v1.0/tasks' % (config['host'], config['port']
    # print url
    resp = requests.get(url)    
    json_data=json.loads(resp.text)
    # print json_data   
    return json_data

# 测试代码
getJson('todo/api/tasks/2016-05-09')