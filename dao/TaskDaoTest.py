#coding=utf-8

'''
Created on 2013-2-25
@author: TonyYu
'''
import TaskDao

    
def testGetTaskListByDate():
    outList = TaskDao.getTaskListByDate('2016-05-06')
    for row in outList:
        print(row)


def testGetTaskListByDateJson():
    outList = TaskDao.getTaskListByDateJson('2016-05-06')
    for row in outList:
   	    print(row)

'''
main 方法
'''
if __name__ == '__main__':
    pass
    testGetTaskListByDate()
    testGetTaskListByDateJson()
    '''
    
    '''