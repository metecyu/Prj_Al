
DROP TABLE IF EXISTS `t_catalog`;
CREATE TABLE `t_catalog` (
  `id` int(11) NOT NULL,
  `fNodeId` int(11) NOT NULL,
  `nodeName` varchar(50) NOT NULL,
  `serNo` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS t_Task ;

CREATE TABLE t_Task (
	id  int NOT NULL ,
	nodeId  int NOT NULL ,
	taskName  varchar(50)  ,
	date  datetime  NOT NULL ,
	userId  varchar(50)  ,
	status  int NOT NULL  ,
	PRIMARY KEY (id)
)


