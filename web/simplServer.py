#coding=utf-8

'''
Created on 2013-2-25
@author: TonyYu
'''
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True,port=8080)