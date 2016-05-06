#coding=utf-8

'''
Created on 2013-2-25
@author: TonyYu
'''
from flask import Flask, jsonify
import sys
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

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    taskList = TaskDao.getTaskListByDateJson('2016-05-06')
    return jsonify({'tasks': tasks}) 

if __name__ == '__main__':
    app.run(debug=True,port=80)