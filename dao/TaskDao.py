#coding=utf-8

'''
Created on 2013-2-25
@author: TonyYu
'''

import mysql.connector

    
'''
    添加一个目录
'''


class Task(): 
    id =-1 # 状态 1：成功 ；0：不成功
    taskName = '' # http code
    status =0 # 花费时间
    


def getTaskListByDate(searchDate):    
    conn = mysql.connector.connect(user='root', password='root', database='db_al')
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

def getTaskListByDateJson(searchDate):
    taskList = getTaskListByDate(searchDate)
 
    taskListJson = []
    for task in taskList:
       taskJson = class_to_dict(task)
       taskListJson.append(taskJson)
    return  taskListJson


def convert_to_dict(obj):
    dict = {}
    dict.update(obj.__dict__)
    return dict
def convert_to_dicts(objs):
    obj_arr = []
    for o in objs:
        #把Object对象转换成Dict对象
        dict = {}
        dict.update(o.__dict__)
        obj_arr.append(dict)
    return obj_arr


def class_to_dict(obj):
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__
    if is_list or is_set:
        obj_arr = []
        for o in obj:
            #把Object对象转换成Dict对象
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict


'''
main 方法
'''
if __name__ == '__main__':
    pass

