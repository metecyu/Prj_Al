import json
import urllib2
url = "http://localhost/todo/api/tasks/2016-05-06"
req = urllib2.Request(url)
f = urllib2.urlopen(req)
httpCodes=f.getcode()
responseStr = f.read() 
f.close() 
print responseStr
json_data=json.loads(responseStr)
print json_data
