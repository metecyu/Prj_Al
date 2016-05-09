#coding=utf-8

'''
Created on 2013-2-25
@author: TonyYu
'''

import mysql.connector
import Db
    
'''
    添加一个目录
'''

def addNode(nodeName,fNodeId):    
    conn = Db.getConn()
    cursor = conn.cursor()
    # 获取id
    cursor.execute('select MAX(id) as id from t_catalog ')
    row = cursor.fetchone()
    newId = row[0]
    if newId == None:
      newId = 500
    newId = newId +1
    # print(newId)
    
    # 计算最大序号
    cursor.execute('select MAX(serNo) as serNo from t_catalog where fnodeId=%s', (fNodeId,))
    row = cursor.fetchone()
    serNo = row[0]
    if serNo == None:
      serNo = 0
    serNo = serNo +1
    # 插入记录
    cursor.execute('insert into t_catalog (id,fnodeId,nodeName,serNo) values (%s,%s, %s,%s)', (newId,fNodeId, nodeName,serNo))     
    
    conn.commit()
    cursor.close()
    return newId

'''
main 方法
'''
if __name__ == '__main__':
    pass
    newId = addNode('根目录',-1)
    print(newId)
    level2 = addNode('二级目录1',newId)
    addNode('二级目录2',newId)

    addNode('三级目录1',level2)
    addNode('三级目录2',level2)         