#coding=utf-8

'''
Created on 2013-2-25
@author: TonyYu
'''
from flask import Flask, jsonify ,Response
import sys
import json 
sys.path.append("..")
from dao import TaskDao



app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'哈Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/tasks/<searchDate>', methods=['GET'])
def get_tasks(searchDate):
    # print searchDate
    taskList = TaskDao.getTaskListByDateJson(searchDate)
    return jsonify({'tasks': taskList}) 


# @app.route("/simple", methods=('POST','GET'))
# def test_simple_view():
#     data = {
#         'hello'  : 'world',
#         'number' : 3
#     }
#     print 11
#     js = json.dumps(data)
#     print 22
#     resp = Response(js, status=200, mimetype='application/json')
#     resp.headers['Link'] = 'http://luisrei.com'
#     return resp   

if __name__ == '__main__':
    app.run(debug=True,port=80) 