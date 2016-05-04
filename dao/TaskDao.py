#coding=utf-8

'''
Created on 2013-2-25
@author: TonyYu
'''

import mysql.connector

    
'''
    添加一个目录
'''
conn = mysql.connector.connect(user='root', password='root', database='db_al')

class Task(): 
    id =-1 # 状态 1：成功 ；0：不成功
    taskName = '' # http code
    status =0 # 花费时间
    


def getTaskListByDate(searchDate):    
    cursor = conn.cursor()
    # 获取id
    cursor.execute('select id,taskName,status from t_task  where date=%s',(searchDate,))

    rows = cursor.fetchall()
    outList =[]
    for row in rows:
       #print(row) 
       task = Task()
       task.id = row[0] 
       task.taskName = row[1]
       task.status = row[2]       
       outList.append(task)
      
    cursor.close()
    conn.close()
    return outList





'''
main 方法
'''
if __name__ == '__main__':
    pass

