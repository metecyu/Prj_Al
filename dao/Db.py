#coding=utf-8

'''
Created on 2013-2-25
@author: TonyYu
'''

import mysql.connector


def getConn():    
    conn = mysql.connector.connect(host='localhost',user='root', password='root', database='db_al')
    return conn

