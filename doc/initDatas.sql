insert into t_catalog (id,fnodeId,nodeName,serNo) values (1,-1,'root',1);
insert into t_catalog (id,fnodeId,nodeName,serNo) values (2,1,'英语',1);
insert into t_catalog (id,fnodeId,nodeName,serNo) values (3,2,'英语学习',1);
insert into t_catalog (id,fnodeId,nodeName,serNo) values (4,3,'voa',1);
insert into t_catalog (id,fnodeId,nodeName,serNo) values (99,1,'其他',1);


insert into t_task (id,nodeId,taskName,date,userId,status) values (1,4,'voa-1','2016-5-2','yzp',0);
insert into t_task (id,nodeId,taskName,date,userId,status) values (2,4,'voa-2','2016-5-2','yzp',0);
insert into t_task (id,nodeId,taskName,date,userId,status) values (3,4,'voa-3','2016-5-2','yzp',0);


-- 2016-5-6
insert into t_task (id,nodeId,taskName,date,userId,status) values (501,99,'python flask 生产一个restful服务(获取任务列表)','2016-5-6','yzp',0);
insert into t_task (id,nodeId,taskName,date,userId,status) values (502,99,'python 调用获取任务列表服务','2016-5-6','yzp',0);
insert into t_task (id,nodeId,taskName,date,userId,status) values (503,99,'查询任务列表的Gui显示','2016-5-6','yzp',0);
insert into t_task (id,nodeId,taskName,date,userId,status) values (504,4,'voa','2016-5-6','yzp',0);