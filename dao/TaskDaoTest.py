#coding=utf-8

'''
Created on 2013-2-25
@author: TonyYu
'''

import TaskDao

    

'''
main 方法
'''
if __name__ == '__main__':
    pass
    outList = TaskDao.getTaskListByDate('2016-05-02')
    for row in outList:
        print(row.id)
    

