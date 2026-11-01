> 迁移自 `C:\Users\Mrwang\Desktop\2024\7-DataBase.md`。图片目录：`../img/`（`1-Note/img`）。

# 数据库与中间件笔记

## 目录

- [SQL 与关系型数据库](#sql-与关系型数据库)
- [MySQL](#mysql)
- [KV 数据库与 Redis](#kv-数据库)
- [Elasticsearch（ES）](#elasticsearches)
- [MongoDB](#mongodb)
- [Neo4j](#neo4j)
- [Hive](#hive)
- [Consul](#consul)
- [时序数据库](#时序数据库)
- [向量数据库](#向量数据库)
- [消息中间件](#消息中间件)
- [负载均衡中间件](#负载均衡中间件)
- [RPC 与 HTTP](#rpc)

---

## SQL 与关系型数据库
### 基本知识

数据库系统实现整体数据结构化，这是数据库的主要特征之一。

数据的共享性高，冗余度低且易扩充

数据独立性高

数据由数据库管理系统统一管理和控制

数据的安全性security保护

防止不合法使用造成数据泄露和破坏

数据的完整性integrity

并发 concurrency 控制

数据库恢复 recovery

### 关系模型

实体 entity

属性 attribute

码 key 唯一标识实体属性集

实体型 entity type

实体集 entity set

联系 relationship

实体-联系方法  Entity-Relationship approch E-R

**关系操作：**
查询 query

选择 select 投影 project 连接 join 除 divide 并 union 差 except 交intersection

插入 insert

删除 delete

修改 update

### 关系的完整性

实体完整性  

primary key主码属性不能为空

参照完整性

用户自定义完整性

```sql
定义表：
create table table_name (
 col1 char(10) primary key , 
 col2 smallint   ,
 col3 smallint   ,
   /*表级完整性约束条件 col1 是外码 ，被参照表是table_name2 */
 foreign key (col1) references table_name2(col) 
   /* primary key(col1,col2,...)*/
) ;
修改表：
alter table <table_nale>
   [	add column<新列名><数据类型>[完整性约束] ]
   [ 	add <表级完整性约束>]
   [	drop [column] <列名>[cascade][restrict]]
   [	drop constraint <完整性约束>[restrict| cascade] ]
   [	alter column <列名> <数据类型>]
删除表
drop table <表名>[restrict | cascade]
restrict : 删除表是有条件的，不能被其他表引用， check , foreign key ,不能有视图触发器，存储过程，或者函数

索引的建立和删除

表的数据量非常大的时候，查询操作非常耗时，建立索引是加快查询的手段
索引有多种类型，
顺序文件上的索引
B+树索引
散列hash
位图索引
创建索引：
create [unique ] [cluster] index <索引名>
on <表名>（<列名>[次序],...）  desc asc（默认是升序）
修改索引：
alter index <旧索引名> rename to <新索引名>
删除索引
drop index <索引名>

数据查询
select [all | distinct] <目标列表达式> [,<目标列表达式>]...
from <表名或者视图名>[,<表名或视图名>...]|(select 语句)[as]<别名>
[where <条件表达式>]
[group by <列名1>[having <条件表达式>]]  //结果按照列名1的值进行分组，属性值相等的元素分为一个组， having 是加入一定的条件
[order by <列名2>[asc | desc ]]   // 按照一个属性列默认升序排序，asc desc 

distinct :  查询某一列，出现重复值， 
where :  短语作用于基本表或者视图 having : 短语作用于组，从中选择满足条件的组
> < = != , and ,or ,not in , between 20 and 30 
字符串匹配： like , % ,_ ,

聚集函数：
count(*)
count([distinct | all]<列明>)
sum()
avg()
max()
min()
注意： where 字句中不能使用聚集函数作为表达式，只能作用于select 和group by 中的having 字句

连接查询
1： 等值连接 （嵌套循环连接） 从第1个表第1条数据 ，去另一个表从头到位匹配，然后组成一个元组。
ex:
select Student.Sno,Sname
from Student , SC 
where Student.Sno = SC.Sno and SC.Cno='2' and SC.Grade > 90
2： 自身连接
	例如查询某个字段的前一个字段  先修课的先修课
3： 外连接
select Student.Sno,Sname
from Student left outer join SC on(Student.Sno = SC.Sno)
4: 多表连接
select Student.Sno,Sname
from Student , SC ,Coure
where Student.Sno = SC.Sno and SC.Cno = Course.Cno
5: 嵌套查询
   select-from-where 定义为查询快
   将一个查询快嵌套在另一个查询快的where ， 或者having 短语中，称为嵌套查询
   注意： order by 字句只能对最终的查询结果排序，字句查询中不能使用order by
  1: 带有 in 谓词的子查询
  2： any all   > all   >=all !=all 
  eg:
  	select Sname ,Sage
  	from Studetn
  	where Sagg < ANY(select Sage from student where Sdept= 'CS')
  	and Sdep <>'CS'
  	首先处理子查询，然后在处理父查询
  3 union、union all、or
  union 联合查询针对每一个查询结果，必须保证列数量、列数据类型及查询顺序一致
  group by 分组查询，根据一个或多个列对结果集进行分组，一般配合聚合函数使用
  
  select  col_1 ,col_2 , ... ,聚合函数...
  from table_name where 条件语句 group by 分组字段  ..having 分组条件
  eg :
  select red_num1 ,count(red_num1)
  from dlt where create_at >='2021-11-01' group by red_num1 hvaing count(red_num1)>=2 ;

其中，having 和 where 使用上有下面区别：
where
在 group by 分组前执行，将查询结果按照条件过滤数据
需要注意的是，where 无法与聚合函数一起使用
having
只能配合 group by 使用，在分组之后执行，用于过滤满足条件的组
需要注意的是，分组是一个耗时的操作，建议在分组前使用 where 对数据进行一次过滤，然后再进行分组
```
### 实践：Join 与查询示例
```
关系性数据库： mysql  postgre  oracle 
redis :
查询内容时添加缓存 ， 
查询数据库之前先查询缓存  ，
https://blog.csdn.net/qq_34090008/article/details/110223773?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0.pc_relevant_default&spm=1001.2101.3001.4242.1&utm_relevant_index=3

大规模数据如何检索:
如何解决单点故障；(lvs、F5、A10、Zookeep、MQ)
如何保证数据安全性；(热备、冷备、异地多活)
如何解决检索难题；(数据库代理中间件：mysql-proxy、Cobar、MaxScale等;)
如何解决统计分析问题；(离线、近实时)
为解决以上问题，从源头着手分析，通常会从以下方式来寻找方法：
1、存储数据时按有序存储；
2、将数据和索引分离；
3、压缩数据；
```
```sql
left join(左联接) 返回包括左表中的所有记录 和右表中联结字段相等的记录  左所有
right join(右联接) 返回包括右表中的所有记录和左表中联结字段相等的记录  
inner join(等值连接) 只返回两个表中联结字段相等的行   相等的
union  连接两个查询  唯一
union all  全部
date_add(data,1)

-- 计算某点到 state 中心距离
SELECT b1.business_id, SQRT(POWER(b1.latitude - b2.avg_lat, 2) +POWER(b1.longitude - b2.avg_long, 2)) as dist
FROM b_etl b1 
INNER JOIN 
(SELECT state, AVG(latitude) as avg_lat, AVG(longitude) as avg_long
FROM b_etl GROUP BY state) b2
ON b1.state = b2.state 
ORDER BY dist DESC


SELECT b.* FROM 
b_etl b 
INNER JOIN outlier o 
ON b.business_id = o.business_id 
WHERE o.dist<10

SELECT state, city, stars, review_count, explode(categories) AS category FROM business

SELECT state, city, stars, review_count, REPLACE(category, ' ','')as new_category FROM part_business_1

SELECT business_id, explode(categories) AS category FROM business

SELECT new_category, AVG(review_count)as avg_review_count 
FROM part_business 
GROUP BY new_category 
ORDER BY avg_review_count DESC

select t1.date,t1.cases - t2.cases as caseIncrease,t1.deaths - t2.deaths as deathIncrease 
from ustotal t1,ustotal t2 
where t1.date = date_add(t2.date,1)

select date,state,sum(cases) as totalCases,sum(deaths) as totalDeaths,round(sum(deaths)/sum(cases),4) as deathRate 
from usInfo 
where date = to_date('2020-05-19','yyyy-MM-dd') 
group by date,state


select 1 as sign,date,'USA' as state,round(sum(totalDeaths)/sum(totalCases),4) as deathRate 
from eachStateInfo 
group by date 
union select 2 as sign,date,state,deathRate 
from eachStateInfo


SELECT Country,SUM(Quantity) AS sumOfQuantity
FROM data 
GROUP BY Country
ORDER BY sumOfQuantity DESC
LIMIT 10


SELECT Country,COUNT(DISTINCT InvoiceNo) AS countOfReturnInvoice 
FROM data 
WHERE InvoiceNo LIKE 'C%' 
GROUP BY Country 
ORDER BY countOfReturnInvoice DESC 
LIMIT 10


SELECT StockCode,AVG(DISTINCT UnitPrice) AS avgUnitPrice,SUM(Quantity) AS sumOfQuantity 
FROM data 
GROUP BY StockCode

```
```http
https://mp.weixin.qq.com/s?__biz=MzI1NzI5NDM4Mw==&mid=2247484048&idx=1&sn=49f970d4421cfd8783808c9d63379074&chksm=ea18ebd0dd6f62c68988bfb894d4e4d9e9bdc2d0d44595f5a98d2df59debfec5ea43541c23d1&token=1376660398&lang=zh_CN&scene=21#wechat_redirect
```
SET @i=0;  # 更新主键id 
UPDATE table_name SET `id`=(@i:=@i+1); 
crate table new_name as select * from table_old  #复制一个表

### 事务与分布式架构
![image-20240609112350239](../img/image-20240609112350239.png)

![image-20240609112359399](../img/image-20240609112359399.png)

#### 分布式事务产生原因：

- 一个请求需要跨多个服务
- 一个请求需要跨多个数据 （数据库/缓存）
- 一个请求需要同时跨多个服务和数据

#### CAP

![image-20240609112712629](../img/image-20240609112712629.png)

![image-20240609112742210](../img/image-20240609112742210.png)



![image-20240609112836947](../img/image-20240609112836947.png)



#### 单体应用拆分

![image-20240609113028361](../img/image-20240609113028361.png)

##### 绞杀者模式

![image-20240609113108463](../img/image-20240609113108463.png)

新模块逐步拆分

![image-20240609113251685](../img/image-20240609113251685.png)

##### 修缮者模式

![image-20240609113233341](../img/image-20240609113233341.png)

![image-20240609113305624](../img/image-20240609113305624.png)

![image-20240609113347068](../img/image-20240609113347068.png)

### 应用架构

![image-20240609113425971](../img/image-20240609113425971.png)

![image-20240609113459411](../img/image-20240609113459411.png)



![image-20240609113516980](../img/image-20240609113516980.png)





![image-20240609113537541](../img/image-20240609113537541.png)

![image-20240609113601638](../img/image-20240609113601638.png)

### 关系型数据库分库分表

![image-20240609113650356](../img/image-20240609113650356.png)

![image-20240609113701616](../img/image-20240609113701616.png)



![image-20240609113729315](../img/image-20240609113729315.png)

![image-20240609113742375](../img/image-20240609113742375.png)



### 微服务异步架构实现

![image-20240609113851961](../img/image-20240609113851961.png)



![image-20240609113907728](../img/image-20240609113907728.png)



微信：大魏分享  分布式事务架构



## MySQL

### 事务、隔离级别与 InnoDB

如果不对事务进行并发控制，我们看看数据库并发操作是会有那些异常情形

- （1）一类丢失更新：两个事物读同一数据，一个修改字段1，一个修改字段2，后提交的恢复了先提交修改的字段。
- （2）二类丢失更新：两个事物读同一数据，都修改同一字段，后提交的覆盖了先提交的修改。
- （3）脏读：读到了未提交的值，万一该事物回滚，则产生脏读。
- （4）不可重复读：两个查询之间，被另外一个事务修改（update）了数据的内容，产生内容的不一致。
- （5）幻读：两个查询之间，被另外一个事务插入或删除了（insert、delete）记录，产生结果集的不一致。

**SQL中的4个事务隔离级别：**

在数据库操作中，为了有效保证并发读取数据的正确性，提出的事务隔离级别。数据库锁，也是为了构建这些隔离级别存在的

| 隔离级别                    | 脏读（Dirty Read） | 不可重复读（NonRepeatable Read） | 幻读（Phantom Read） |
| --------------------------- | ------------------ | -------------------------------- | -------------------- |
| 读未提交(Read uncommitted） | 可能               | 可能                             | 可能                 |
| 读已提交（Read committed）  | 不可能             | 可能                             | 可能                 |
| 可重复读（Repeatable read） | 不可能             | 不可能                           | 可能                 |
| 可串行化（Serializable ）   | 不可能             | 不可能                           | 不可能               |

**（1）读未提交**

未提交意味着这些数据可能会回滚，也就是可能最终不会存到数据库中，也就是不存在的数据。

读到了并一定最终存在的数据，这就是脏读。

**允许脏读。**在 **读未提交** 隔离级别下，允许 **脏读** 的情况发生。

<img src="../img/image-20231023205059240.png" alt="image-20231023205059240" style="zoom:50%;" />

1： 开始事物

2： 更新数据

3： 读取到未提交的数据

4： 回滚了事物

事务B的更新数据被事务A读取，但是事务B回滚了，更新数据全部还原，也就是说事务A刚刚读到的数据并没有存在于数据库中。

**（2）读已提交**

在 **读已提交** 隔离级别下，**禁止了 脏读**，但是 允许**不可重复读**的情况发生

![image-20231023205835935](../img/image-20231023205835935-1716730541873.png)

**（3）可重复读**

在**可重复读**隔离级别下，禁止了：**脏读、不可重复读**。但是，允许**幻读**。

在可重复读中，该sql第一次读取到数据后，就将这些数据加锁（悲观锁），其它事务无法修改这些数据，就可以实现可重复读了。

但这种方法却无法锁住insert的数据，所以当事务A先前读取了数据，或者修改了全部数据，事务B还是可以insert数据提交，

这时事务A就会发现莫名其妙多了一条之前没有的数据，这就是幻读，不能通过行锁来避免。

**（4）串行化**

```text
最严格的事务，要求所有事务被串行执行，不能并发执行。
```

MySQL默认事务隔离级别为可重复读(RR)

MySQL 的InnoDB （InnoDB 是 MySQL 的一个存储引擎）

InnoDB 是通过 日志和锁 来保证的事务的 ACID特性，具体如下：

（1）通过数据库锁的机制，保障事务的隔离性；

（2）通过 Redo Log（重做日志）来，保障事务的持久性；

（3）通过 Undo Log （撤销日志）来，保障事务的原子性；

**Undo Log 如何保障事务的原子性呢？**

具体的方式为：在操作任何数据之前，首先将数据备份到一个地方（这个存储数据备份的地方称为 Undo Log），然后进行数据的修改。如果出现了错误或者用户执行了 Rollback 语句，系统可以利用 Undo Log 中的备份将数据恢复到事务开始之前的状态。

具体的方式为：Redo Log 记录的是新数据的备份（和 Undo Log 相反）。在事务提交前，只要将 Redo Log  持久化即可，不需要将数据持久化。当系统崩溃时，虽然数据没有持久化，但是 Redo Log 已经持久化。系统可以根据 Redo Log  的内容，将所有数据恢复到崩溃之前的状态。

**脏读、幻读、不可重复读**

在多个事务并发操作时，数据库中会出现下面三种问题：**脏读，幻读，不可重复读**。

**脏读（Dirty Read）**

事务A读到了事务B还未提交的数据：

**幻读（Phantom Read）**

事务A进行范围查询时，事务B中新增了满足该范围条件的记录，当事务A再次按该条件进行范围查询，会查到在事务B中提交的新的满足条件的记录（**幻行** Phantom Row）。

**不可重复读（Unrepeatable Read）**

事务A在读取某些数据后，再次读取该数据，发现读出的该数据已经在事务B中发生了变更或删除。



- **幻读**：在同一事务中，相同条件下，两次查询出来的 **记录数** 不一样；
- **不可重复读**：在同一事务中，相同条件下，两次查询出来的 **数据** 不一样；

DDL : data definition language 

### 客户端连接与 DDL 速查

```bash
# DBMS (关系型数据库管理系统)
# connect database
mysql -u user -p
update mysql.user set authentication_string=passowrd('123456') where user='root' and host = 'localhost'

DDL  Database Language
DML 
DQL 
DCL 

CRUD 
show create database database_name # 查看创建数据库创建语句
desc table_name  # 查看表的结构

数据库引擎 

数据表的类型 ：
Innodb: 默认使用 
MyISAM: 
create
select 
insert 
update
delete  # 不会影响自增 
truncate # 清空表 自增会归0 


```

![image-20230406221458907](../img/image-20230406221458907.png)



![image-20230406221601618](../img/image-20230406221601618.png)

![image-20230406222047081](../img/image-20230406222047081.png)

分页和排序

limit orderby 

![image-20230406223121004](../img/image-20230406223121004.png)





![image-20230505212117166](../img/image-20230505212117166-1716638295720.png)

![image-20230505212148508](../img/image-20230505212148508-1716638295719.png)

![image-20230505212200168](../img/image-20230505212200168-1716638295720.png)

![image-20230505212345951](../img/image-20230505212345951-1716638295721.png)



![image-20230505212423502](../img/image-20230505212423502-1716638295720.png)

![image-20230505212809969](../img/image-20230505212809969-1716638295721.png)

![image-20230505212936006](../img/image-20230505212936006-1716638295721.png)



![image-20230505213115436](../img/image-20230505213115436-1716638295721.png)



![image-20230505213422579](../img/image-20230505213422579-1716638295721.png)

![image-20230505213515128](../img/image-20230505213515128-1716638295721.png)



![image-20230505213618483](../img/image-20230505213618483-1716638295721.png)



![image-20230505213939656](../img/image-20230505213939656-1716638295721.png)



![image-20230505214024554](../img/image-20230505214024554-1716638295721.png)





![image-20230505214047848](../img/image-20230505214047848-1716638295721.png)



![image-20230505214123286](../img/image-20230505214123286-1716638295721.png)



![image-20230505214200387](../img/image-20230505214200387-1716638295721.png)

![image-20230505214229628](../img/image-20230505214229628-1716638295721.png)



![image-20230505214303248](../img/image-20230505214303248-1716638295722.png)



![image-20230505214345732](../img/image-20230505214345732-1716638295722.png)



![image-20230505214543138](../img/image-20230505214543138-1716638295722.png)





![image-20230505214633952](../img/image-20230505214633952-1716638295722.png)



![image-20230505214725812](../img/image-20230505214725812-1716638295722.png)



![image-20230505214848780](../img/image-20230505214848780-1716638295722.png)



![image-20230505214933150](../img/image-20230505214933150-1716638295722.png)

![image-20230505215215540](../img/image-20230505215215540-1716638295722.png)





![image-20230505215342472](../img/image-20230505215342472-1716638295722.png)



![image-20230505215408336](../img/image-20230505215408336-1716638295722.png)

![image-20230505215502852](../img/image-20230505215502852-1716638295722.png)



![image-20230505215705031](../img/image-20230505215705031-1716638295722.png)

![image-20230505215835336](../img/image-20230505215835336-1716638295722.png)



![image-20230505215941394](../img/image-20230505215941394-1716638295722.png)



![image-20230505220321376](../img/image-20230505220321376-1716638295723.png)

![image-20230505220348081](../img/image-20230505220348081-1716638295723.png)

![image-20230505220540625](../img/image-20230505220540625-1716638295723.png)



![image-20230505220700585](../img/image-20230505220700585-1716638295723.png)

![image-20230505220728347](../img/image-20230505220728347-1716638295723.png)

![image-20230505220808498](../img/image-20230505220808498-1716638295723.png)



![image-20230505220844619](../img/image-20230505220844619-1716638295723.png)



![image-20230505221051013](../img/image-20230505221051013-1716638295723.png)

![image-20230505221112338](../img/image-20230505221112338-1716638295723.png)

![image-20230505221358508](../img/image-20230505221358508-1716638295723.png)





## KV 数据库
### Redis
docker search redis 
docker pull redis 


docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 6379:6379 --name myredis -v /home/redis/myredis/myredis.conf:/etc/redis/redis.conf -v /home/redis/myredis/data:/data -d redis redis-server /etc/redis/redis.conf  --appendonly yes  --requirepass 123456

#### 基本概念

Remote Dictionary Server **基于内存的且支持持久化，高性能的Key-Value的NOSQL数据库**

5大基本类型：

- String: 字符串
- Hash: 散列
- List: 列表
- Set: 集合
- Sorted Set: 有序集合 zset

Redis also includes:

- [Transactions](https://redis.io/topics/transactions)
- [Pub/Sub](https://redis.io/topics/pubsub)
- [Lua scripting](https://redis.io/commands/eval)
- [Keys with a limited time-to-live](https://redis.io/commands/expire)
- [LRU eviction of keys](https://redis.io/docs/reference/eviction)
- [Automatic failover](https://redis.io/topics/sentinel)

#### 特点：

- 速度快
  \- 单节点读 110000次/s，写81000次/s

- - 数据存放内存中
  - 用 C 语言实现，离操作系统更近
  - 单线程架构，6.0 开始支持多线程（CPU、IO 读写负荷）

- 持久化

- - 数据的更新将异步地保存到硬盘（RDB 和 AOF）

- 多种数据结构 - 不仅仅支持简单的 key-value 类型数据，还支持：字符串、hash、列表、集合、有序集合，

- 功能丰富
  \- HyperLogLog、GEO、发布订阅、Lua脚本、事务、Pipeline、Bitmaps，key 过期

- 简单稳定
  \- 源码少、单线程模型

- 主从复制

- Redis 支持数据的备份（master-slave）与集群（分片存储），以及拥有哨兵监控机制。

- Redis 的所有操作都是原子性的，同时 Redis 还支持对几个操作合并后的原子性执行。

#### 使用场景

##### cache

计数器

消息队列

#### 基本使用

##### global commands:

```sql
keys：查看所有键
dbsize：键总数
exists key：检查键是否存在
del key [key ...]：删除键
expire key seconds：键过期
ttl key: 通过 ttl 命令观察键键的剩余过期时间
type key：键的数据结构类型
```

##### string

常用字符串命令

```
set key value [ex seconds][px milliseconds] [nx|xx]: 设置值，返回 ok 表示成功
	ex seconds:为键设置秒级过期时间。
	px milliseconds:为键设置毫秒级过期时间。
	nx:键必须不存在，才可以设置成功，用于添加。可单独用 setnx 命令替代
	xx:与 nx 相反，键必须存在，才可以设置成功，用于更新。可单独用 setxx 命令替代
	
get key：获取值
mset key value [key value ...]：批量设置值，批量操作命令可以有效提高业务处理效率
mget key [key ...]：批量获取值，批量操作命令可以有效提高业务处理效率

incr key：计数，返回结果分 3 种情况：
	值不是整数，返回错误。
	值是整数，返回自增后的结果。
	键不存在，按照值为 0 自增，返回结果为 1。

decr(自减)、incrby(自增指定数字)、 decrby(自减指定数字)
incrby by num 3


```
字符串使用场景：

1. 缓存数据，提高查询性能。比如存储登录用户信息、电商中存储商品信息
2. 可以做计数器（想知道什么时候封锁一个 IP 地址(访问超过几次)）,短信限流
3. 共享 Session，例如：一个分布式 Web 服务将用户的 Session 信息(例如用户登录信息)保存在各自服务器中，这样会造成一个问题，出于负载均衡的考虑，分布式服务会将用户的访问均衡到不同服务器上，用户刷新一次访问可 能会发现需要重新登录，为了解决这个问题，可以使用 Redis 将用户的 Session 进行集中管理，在这种模式下只要保证 Redis 是高可用和扩展性的，每次用户 更新或者查询登录信息都直接从 Redis 中集中获取，如图：

<img src="../img/image-20231009212625087.png" alt="image-20231009212625087" style="zoom:50%;" />



#####  hash 

内部是无序字典,一个哈希表有多个节点，每个节点保存一个键值对

```
hset key field value：设置值
	hset student name xiaoming age 18 
hget key field：获取值
	hget student name 
hdel key field [field ...]：删除 field
hlen key：计算 field 个数
hmset key field value [field value ...]：批量设置 field-value
hmget key field [field ...]：批量获取 field-value
hexists key field：判断 field 是否存在
hkeys key：获取所有 field
hvals key：获取所有 value
hgetall key：获取所有的 field-value
incrbyfloat 和 hincrbyfloat:就像 incrby 和 incrbyfloat 命令一样，但是它们的作 用域是 filed
```
**哈希使用场景**

Hash 也可以同于对象存储，比如存储用户信息，与字符串不一样的是，字符串是需要将对象进行序列化（比如 json 序列化）之后才能保存，而 Hash 则可以讲用户对象的每个字段单独存储，这样就能节省序列化和反序列的时间。如下：

##### lists:

```
rpush key value [value ...]：从右边插入元素
lpush key value [value ...]：从左边插入元素
linsert key before|after pivot value：向某个元素前或者后插入元素
lrange key start end：获取指定范围内的元素列表，lrange key 0 -1可以从左到右获取列表的所有元素
lindex key index：获取列表指定索引下标的元素
llen key：获取列表长度
lpop key：从列表左侧弹出元素
rpop key：从列表右侧弹出
lrem key count value：删除指定元素，lrem 命令会从列表中找到等于 value 的元素进行删除，根据 count 的不同 分为三种情况:
    count>0，从左到右，删除最多 count 个元素。
    count<0，从右到左，删除最多 count 绝对值个元素。
    count=0，删除所有。

ltrim key start end：按照索引范围修剪列表
lset key index newValue：修改指定索引下标的元素
blpop key [key ...] timeout 和 brpop key [key ...] timeout：阻塞式弹出
```
**列表使用场景**

1. 热销榜，文章列表
2. 实现工作队列（利用 lists 的 push 操作，将任务存在 lists 中，然后工作线程再用 pop 操作将任务取出进行执行 ），例如消息队列
3. 最新列表，比如最新评论

使用参考：

- lpush+lpop=Stack(栈)
- lpush+rpop=Queue(队列)
- lpsh+ltrim=Capped Collection(有限集合)
- lpush+brpop=Message Queue(消息队列)

##### set 

Redis 的集合相当于 Java 语言里面的 HashSet 和 JS 里面的 Set，它内部的键值对是无序的**唯一**的。Set 集合中最后一个 value 被移除后，数据结构自动删除，内存被回收。

```
sadd key element [element ...]：添加元素，返回结果为添加成功的元素个数
srem key element [element ...]：删除元素，返回结果为成功删除元素个数
smembers key：获取所有元素
sismember key element：判断元素是否在集合中，如果给定元素 element 在集合内返回 1，反之返回 0
scard key：计算元素个数，scard 的时间复杂度为 O(1)，它不会遍历集合所有元素
spop key：从集合随机弹出元素，从 3.2 版本开始，spop 也支持[count]参数。
srandmember key [count]：随机从集合返回指定个数元素，[count]是可选参数，如果不写默认为 1
sinter key [key ...]：求多个集合的交集
suinon key [key ...]：求多个集合的并集
sdiff key [key ...]：求多个集合的差集
```
##### zset

zset 可能是 Redis 提供的最为特色的数据结构，它也是在面试中面试官最爱问的数据结构。它类似于 Java 的 SortedSet 和 HashMap 的结合体，一方面它是一个 set，保证了内部 value 的唯一性，另一方面它可以给每个 value 赋予一个 score，代表这个 value 的排序权重。它的内部实现用的是一种叫着「跳跃列表」(后面会简单介绍)的数据结构。

```
zadd key score member [score member ...]：添加成员，返回结果代表成功添加成员的个数。Redis3.2 为 zadd 命令添加了 nx、xx、ch、incr 四个选项:
    nx:member 必须不存在，才可以设置成功，用于添加
    xx:member 必须存在，才可以设置成功，用于更新
    ch:返回此次操作后，有序集合元素和分数发生变化的个数
    incr:对 score 做增加，相当于后面介绍的 zincrby

zcard key：计算成员个数
zscore key member：计算某个成员的分数
zrank key member 和 zrevrank key member：计算成员的排名，zrank 是从分数从低到高返回排名，zrevrank 反之
zrem key member [member ...]：删除成员
zincrby key increment member：增加成员的分数
zrange key start end [withscores] 和 zrevrange key start end [withscores]：返回指定排名范围的成员，zrange 是从低到高返回，zrevrange 反之。
zrangebyscore key min max [withscores][limit offset count] 和 zrevrangebyscore key max min [withscores][limit offset count] 返回指定分数范围的成员，其中 zrangebyscore 按照分数从低到高返回，zrevrangebyscore 反之
zcount key min max：返回指定分数范围成员个数
zremrangebyrank key start end：删除指定排名内的升序元素
zremrangebyscore key min max：删除指定分数范围的成员
zinterstore 和 zunionstore 命令求集合的交集和并集，可用参数比较多，可用到再查文档
```
**集合和有序集合使用场景**

1. 给用户添加标签
2. 给标签添加用户
3. 根据某个权重进行排序的队列的场景，比如游戏积分排行榜，

 Redis 客户端执行一条命令的过程：

<img src="../img/image-20231010205237113.png" alt="image-20231010205237113" style="zoom:50%;" />

**慢查询分析**：

所谓慢查询日志就是系统在命令执行前后计算每条命令的执行时间，当超过预设阈值，就将这条命令的相关信息（例如：发生时间，耗时，命令的详细信息）记录下来

**Pipeline（流水线）机制**

Redis 提供了批量操作命令（例如 mget、mset 等

#### 事物和exec 命令

一次执行不止一个命令，而且需要其同时成功或者失败。为了保证多条命令组合的原子性，Redis 提供了简单的事务功能以及集成 Lua 脚本来解决这个问题

Redis 提供了简单的事务功能，将一组需要一起执行的命令放到 multi 和 exec 两个命令之间。Multi 命令代表事务开始，exec 命令代表事务结束，它们之间的命令是原子顺序执行的

```
multi
	command1
	command2
	...
exec 
```
#### **发布订阅**

<img src="../img/image-20231010205851026.png" alt="image-20231010205851026" style="zoom:50%;" />

```sql
subscribe channel [channel ...] # 订阅一个或多个频道
unsubscribe channel # 退订指定频道
publish channel message # 发送消息
psubscribe pattern # 订阅指定模式
punsubscribe pattern # 退订指定模式
```
 Redis 发布的消息不会被持久化，这就会导致新订阅的客户端将不会收到历史消息。所以，如果当前的业务场景不能容忍这些缺点，那还是用专业 MQ 吧。

#### **持久化、主从同步与缓存设计**

Redis 支持 RDB 和 AOF 两种持久化机制,持久化功能有效地避免因进程 退出造成的数据丢失问题，当下次重启时利用之前持久化的文件即可实现数据恢复。











https://redis.io/docs/

https://redis.com.cn/documentation.html

https://zhuanlan.zhihu.com/p/573593502?utm_id=0

https://zhuanlan.zhihu.com/p/469102289

https://zhuanlan.zhihu.com/p/469102289

## Elasticsearch（ES）

```text
倒排索引
索引 ：  dataset
https://blog.csdn.net/u011863024/article/details/115721328
索引 Index 
类型 type
文档 document  JSON 
字段 fild 
映射 Mapping 是处理数据的方式 ，和规则方面做的一些限制 ，
分片 shards 
副本 Replicas  分片的副本 高可用 
分配 allocation  
倒排索引
分词器
安装
基本使用 
高级应用
```

```python
# 镜像与基本 API
docker pull elasticsearch:7.7.0
docker run --name elasticsearch -d -e ES_JAVA_OPTS="-Xms512m -Xmx512m" -e "discovery.type=single-node" -p 9200:9200 -p 9300:9300 elasticsearch:7.12.0
#运行kibana 注意IP一定不要写错
docker run --name kibana -e ELASTICSEARCH_HOSTS=http://192.168.5.6:9200 -p 5601:5601 -d kibana:7.12.0

es提供了一套api，叫做cat api，可以查看es中各种各样的数据
GET /_cat/health?v
GET /_cat/indices?v
创建索引：
PUT 
	/demo_index
	/book
删除索引
DELETE
	/demo_index
	/book
新增文档:
POST 
	/index/type/id
	/book/_doc/1
	{json 数据}
检索文档：
GET
	/index/type/id
	/book/_doc/1
替换操作：
POST
	PUT /book/_doc/1
	{}
更新文档：
POST
	/{index}/type /{id}/_update
	/{index}/_update/{id}
删除文档：
DELETE 
	/book/_doc/1
	
	
mget 批量查询：
POST /_bulk

index  分片 shard  ()
{
   "settings" : {
      "number_of_shards" : 3, # 分片个数
      "number_of_replicas" : 1 # 副本
   }

单节点： 单点故障 
水平扩容 
	加入新的节点： 主分片定下来，就不能修改，副本分片可以调整数量
	
增删改可以看做update,都是对数据的改动。一个改动请求发送到es集群，经历以下四个步骤：

（1）客户端选择一个node发送请求过去，这个node就是coordinating node（协调节点）找主分片
在主节点进行业务操作
（2）coordinating node，对document进行路由，将请求转发给对应的node（有primary shard）
（3）实际的node上的primary shard处理请求，然后将数据同步到replica node。
（4）coordinating node，如果发现primary node和所有replica node都搞定之后，就返回响应结果给客户端。


词条
词典
倒排表
    
    
dynamic mapping：
 自动为我们建立index，以及对应的mapping，mapping中包含了每个field对应的数据类型，以及如何分词等设置。
    
tf-idf
tf : term-frequence 词频
idf : verse-document frequence
```

预定义 logical form 模板：

实体检索

实体属性检索

实体属性多跳检索

多种属性条件检索实体

jieba 分词

数据类型：

text : 文本类型 分词

keywords:  不会被分词

数组类型 ： []  都要一样

映射参数：

index  默认为true 

flase ，这该字段不会被创建索引，但是可以在source 元数据中展示 调优



![image-20230802214536778](../img/image-20230802214536778.png)

analyzer ： 分词词

boost ： 当前设置评分的权重

coerce ： 是否能强制类型转换

copy_to

doc_values ： text  默认false 

![image-20230802215823944](../img/image-20230802215823944.png)







## MongoDB
MongoDB 是一款流行的开源文档型数据库，分布式

1. 面向文档存储，基于JSON/BSON 可表示灵活的数据结构
2. 动态 DDL能力，没有强Schema约束，支持快速迭代
3. 高性能计算，提供基于内存的快速数据查询
4. 容易扩展，利用数据分片可以支持海量数据存储
5. 丰富的功能集，支持二级索引、强大的聚合管道功能，为开发者量身定做的功能，如数据自动老化、固定集合等等。
6. 跨平台版本、支持多语言SDK.

database:

collection:

document:

field :

```sqlite
use database_name # 创建数据库 
show dbs 
db 
db.dropDatabase()
# 显示创建
db.createCollection(name)
show colletions /show tables 
df.colletion_name.drop()

CRUD :


```
存储机制：

​	内存

​	磁盘

## Neo4j

```text
属性图
    节点 Node (可以包含多个属性property 和标签 label)
    属性
    关系: edge ,可以有多个property , 但是只能有一个类型type
    标签: 
    数据浏览器
```
![image-20230405153637462](../img/image-20230405153637462-1716637638724.png)

![image-20230405153556494](../img/image-20230405153556494-1716637638726.png)

<img src="../img/image-20230405154948374.png" alt="image-20230405154948374" style="zoom:50%;" />

```cypher
cypyter : CQL
(identify:label{property})  : 表示节点
标识符：就是起的变量名，用来保存节点，后面也可以使用他来引用。
标签：代表节点的类型，节点可以有多个标签，也可以没有。
属性：花括号{}代表节点的属性，属性类似Python的字典。
--
- >
< - 
-[identify:label{property}]- >
[] 

match (n:Label) return n
```

## Hive

```shell
Hive支持基本数据类型和复杂类型,
基本数据类型主要有数值类型(INT、FLOAT、DOUBLE ) 、布尔型和字符串
复杂数据类型：
ARRAY: 有序字段
MAP: 无序字段
STRUCT: 一组命名的字段
HiveQL操作命令：
数据定义、数据操作
除 dbproperties属性外，数据库的元数据信息都是不可更改的，包括数据库名和数据库所在的目录位置，没有办法删除或重置数据库属性。
https://dblab.xmu.edu.cn/blog/1080-2/

https://zhuanlan.zhihu.com/p/100163942
https://zhuanlan.zhihu.com/p/103413663

1：Hive 查询原理：
hive 其实是将hql转成MR程序
元数据 是hive 表的一些参数 不是hdfs 上的数据
在执行查询操作时 ,先从元数据库中找到 对应表对应的文件位置
通过 hive的解析器、编译器、优化器 执行器 将 sql 语句 转换成 MR 程序，运行在 Yarn 上，最终得到结果。
Hive 是将数据映射成数据库和一张张的表，库和表的元数据信息一般存在关系型数据库上（比如 MySQL）
Hive 本身并不提供数据的存储功能，数据一般都是存储在 HDFS 上的（对数据完整性、格式要求并不严格）
MetaStore：存储和管理Hive的元数据，使用关系数据库来保存元数据信息。


2： 内部表和外部表
内部表会移动数据到指定位置 ，将数据文件移动到默认位置，一般都是/usr/hive/warehouse/ 目录下
外部表不会移动数据，数据在哪就是哪
内部表删除，数据一起删除
外部表不会删除数据
工作中使用外部表做为数据映射，而统计出的结果一般多使用内部表，因为内部表仅仅用于储存结果或者关联，与 HDFS 数据无关。
desc formatted 表名即可查看。 是否内部表 外部表


分区表
动态分区
静态分区
分桶表 超大数据
分桶表一般在超大数据时才会使用，分桶将整个数据内容按某列属性值取hash值进行区分，具有相同hash值的数据进入到同一个文件中，意味着原本属于一个文件的数据经过分桶后会落到多个文件中。

倾斜表
临时表

复合数据类型：
Hive 中复合数据类型有 Array、Map、Struct 这三种

Array 代表数组，类型相同的数据
Map 映射 k--v 对
Struct 则存储类型不同的一组数据


CREATE (DATABASE|SCHEMA) [IF NOT EXISTS] database_name   --DATABASE|SCHEMA 是等价的
  [COMMENT database_comment] --数据库注释
  [LOCATION hdfs_path] --存储在 HDFS 上的位置
  [WITH DBPROPERTIES (property_name=property_value, ...)]; --指定额外属性
describe database hive_test;

#删除数据库
DROP (DATABASE|SCHEMA) [IF EXISTS] database_name [RESTRICT|CASCADE];


CREATE [TEMPORARY] [EXTERNAL] TABLE [IF NOT EXISTS] [db_name.]table_name     --表名
  [(col_name data_type [COMMENT col_comment],
    ... [constraint_specification])]  --列名 列数据类型
  [COMMENT table_comment]   --表描述
  [PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)]  --分区表分区规则
  [
    CLUSTERED BY (col_name, col_name, ...) 
   [SORTED BY (col_name [ASC|DESC], ...)] INTO num_buckets BUCKETS
  ]  --分桶表分桶规则
  [SKEWED BY (col_name, col_name, ...) ON ((col_value, col_value, ...), (col_value, col_value, ...), ...)  
   [STORED AS DIRECTORIES] 
  ]  --指定倾斜列和值
  [
   [ROW FORMAT row_format]    
   [STORED AS file_format]
     | STORED BY 'storage.handler.class.name' [WITH SERDEPROPERTIES (...)]  
  ]  -- 指定行分隔符、存储文件格式或采用自定义存储格式
  [LOCATION hdfs_path]  -- 指定表的存储位置
  [TBLPROPERTIES (property_name=property_value, ...)]  --指定表的属性
  [AS select_statement];   --从查询结果创建表

# 通过查询建立表
CREATE TABLE emp_copy AS SELECT * FROM emp WHERE deptno='20';
CREATE [TEMPORARY] [EXTERNAL] TABLE [IF NOT EXISTS] [db_name.]table_name  --创建表表名
   LIKE existing_table_or_view_name  --被复制表的表名
   [LOCATION hdfs_path]; --存储位置
CREATE TEMPORARY EXTERNAL TABLE  IF NOT EXISTS  emp_co  LIKE emp

加载数据到表
load data local inpath "/usr/file/emp.txt" into table emp;
重命名表
ALTER TABLE table_name RENAME TO new_table_name;
修改列

查询结果插入表
INSERT OVERWRITE TABLE tablename1 [PARTITION (partcol1=val1, partcol2=val2 ...) [IF NOT EXISTS]]   
select_statement1 FROM from_statement;

INSERT INTO TABLE tablename1 [PARTITION (partcol1=val1, partcol2=val2 ...)] 
select_statement1 FROM from_statement


导出数据
INSERT OVERWRITE [LOCAL] DIRECTORY directory1
  [ROW FORMAT row_format] [STORED AS file_format] 
  SELECT ... FROM ...
 
# 累计窗口 函数
sum() over()
avg() over()
# 排序窗口函数
rank() over()
dense_rank() over()
row_number() over()

```

### PySpark / Hive SQL 练习（Yelp）

```python
# 分列
split_col = f.split(business['categories'], ',')
# 重命名、过滤掉空的数据
business = business.withColumn("categories", split_col).filter(business["city"] != "").dropna()
# 临时表
business.createOrReplaceTempView("business")
# 筛选列
b_etl = spark.sql(
    "SELECT business_id, name, city, state, latitude, longitude, stars, review_count, is_open, categories, attributes FROM business"
).cache()

# 到某店到 state center 的距离
outlier = spark.sql(
    "SELECT b1.business_id, SQRT(POWER(b1.latitude - b2.avg_lat, 2) + POWER(b1.longitude - b2.avg_long, 2)) "
    "as dist FROM b_etl b1 INNER JOIN (SELECT state, AVG(latitude) as avg_lat, AVG(longitude) as avg_long "
    "FROM b_etl GROUP BY state) b2 ON b1.state = b2.state ORDER BY dist DESC"
)

# 内连接
joined = spark.sql(
    "SELECT b.* FROM b_etl b INNER JOIN outlier o ON b.business_id = o.business_id WHERE o.dist<10"
)
# explode 拆行
part_business = spark.sql(
    "SELECT state, city, stars, review_count, explode(categories) AS category FROM business"
).cache()

spark.sql("SELECT COUNT(DISTINCT(new_category)) FROM part_business")
spark.sql("SELECT new_category, COUNT(*) as freq FROM part_business GROUP BY new_category ORDER BY freq DESC")
spark.sql("SELECT city, new_category, COUNT(*) as freq FROM part_business GROUP BY city, new_category ORDER BY freq DESC")
spark.sql("SELECT city, COUNT(business_id) as no_of_busy FROM business GROUP BY city ORDER BY no_of_bus DESC")

df.toJSON()
df.toPandas()
```

### Hive SQL 速查（教程摘录）

```text
一文学完所有的Hive Sql（两万字最全详解） 五分钟学大数据  
1： 基本概念
存储格式： textfile ,sequencefile(binary insert 加载) rcfile(行列混合压缩) orc


2： 基本操作 
DDL : 
创建，修改数据库
表： 内部表，外部表，分区表。分桶表
单表的查询，关联查询
hive 函数： 聚合函数,条件函数，日期函数 ，字符串函数
行转列,列转行  ： lateral view , explode  reflect
窗口函数 
分析函数
3： 语法知识 

#对数据库的操作 
创建数据库
create database if not exists myhive;
说明：hive的表存放位置模式是由hive-site.xml当中的一个属性指定的:hive.metastore.warehouse.dir

创建数据库并指定hdfs存储位置 :
create database myhive2 location '/myhive2';

查看数据库详细信息
desc database  myhive2;
desc database extended  myhive2; 查看数据库更多详细信息

删除数据库
drop  database  myhive2;
强制删除数据库，包含数据库下面的表一起删除
drop  database  myhive  cascade; 

#对数据表的操作
	建内部表
create  table 
if not exists stu2(id int ,name string) 
row format delimited fields terminated by '\t' 
stored as textfile 
location '/user/stu2';
row format delimited fields terminated by '\t' 指定字段分隔符，默认分隔符为 '\001'
stored as 指定存储格式
location 指定存储位置

根据查询结果创建表
create table stu3 as select * from stu2;
根据已经存在的表结构创建表
create table stu4 like stu2;
查询表的结构
desc stu2;
详细查询
desc formatted  stu2;
查询创建表的语句
show create table stu2;

#对外部表操作
外部表因为是指定其他的hdfs路径的数据加载到表当中来，所以hive表会认为自己不完全独占这份数据，所以删除hive表的时候，数据仍然存放在hdfs当中，不会删掉，只会删除表的元数据

构建外部表
create external table student (s_id string,s_name string) 
row format delimited fields terminated by '\t';
从本地文件系统向表中加载数据
追加操作
load data local inpath '/export/servers/hivedatas/student.csv' into table student;
覆盖操作
load data local inpath '/export/servers/hivedatas/student.csv' overwrite  into table student;
从hdfs文件系统向表中加载数据
load data inpath '/hivedatas/techer.csv' into table techer;
加载数据到指定分区
load data inpath '/hivedatas/techer.csv' into table techer partition(cur_date=20201210);

1.使用 load data local 表示从本地文件系统加载，文件会拷贝到hdfs上
2.使用 load data 表示从hdfs文件系统加载，文件会直接移动到hive相关目录下，注意不是拷贝过去，因为hive认为hdfs文件已经有3副本了，没必要再次拷贝了
3.如果表是分区表，load 时不指定分区会报错
4.如果加载相同文件名的文件，会被自动重命名

#对分区表的操作
创建分区表的语法
create table score(s_id string, s_score int) partitioned by (month string);
创建一个表带多个分区
create table score2 (s_id string, s_score int) partitioned by (year string,month string,day string);
加载数据到一个分区的表中
load data local inpath '/export/servers/hivedatas/score.csv' into table score partition (month='201806');
加载数据到一个多分区的表中去
load data local inpath '/export/servers/hivedatas/score.csv' into table score2 partition(year='2018',month='06',day='01');
当表是分区表时，比如 partitioned by (day string)， 则这个文件夹下的每一个文件夹就是一个分区，且文件夹名为 day=20201123 这种格式，然后使用：msck  repair   table  score; 修复表结构，成功之后即可看到数据已经全部加载到表当中去了

查看分区
show  partitions  score;
添加一个分区
alter table score add partition(month='201805');
同时添加多个分区
alter table score add partition(month='201804') partition(month = '201803');
注意：添加分区之后就可以在hdfs文件系统当中看到表下面多了一个文件夹
删除分区
alter table score drop partition(month = '201806');

#对分桶表操作
将数据按照指定的字段进行分成多个桶中去，就是按照分桶字段进行哈希划分到多个文件当中去
分区就是分文件夹，分桶就是分文件
分桶优点：
1. 提高join查询效率
2. 提高抽样效率
开启hive的捅表功能
set hive.enforce.bucketing=true;
设置reduce的个数
set mapreduce.job.reduces=3;

创建桶表
create table course (c_id string,c_name string) 
clustered by(c_id) into 3 buckets;

桶表的数据加载：由于桶表的数据加载通过hdfs  dfs  -put文件或者通过load  data均不可以，只能通过insert  overwrite 进行加载所以把文件加载到桶表中，需要先创建普通表，并通过insert  overwrite的方式将普通表的数据通过查询的方式加载到桶表当中去

通过insert overwrite给桶表中加载数据
insert overwrite table course 
select * from course_common cluster by(c_id);  -- 最后指定桶字段


#修改表和删除表
修改表名称
alter table  old_table_name  rename to new_table_name;
增加/修改列信息
查询表结构
desc score5;
添加列
alter table score5 add columns (mycol string, mysco string);
更新列
alter table score5 change column mysco mysconew int;
删除表操作
drop table score5;
清空表操作
truncate table score6;
说明：只能清空管理表，也就是内部表；清空外部表，会产生错误

如果 hdfs 开启了回收站，drop 删除的表数据是可以从回收站恢复的，表结构恢复不了，需要自己重新创建；truncate 清空的表是不进回收站的，所以无法恢复truncate清空的表
所以 truncate 一定慎用，一旦清空将无力回天

#向hive表中加载数据
直接向分区表中插入数据
insert into table score partition(month ='201807') values ('001','002','100');
通过load方式加载数据
load data local inpath '/export/servers/hivedatas/score.csv' overwrite into table score partition(month='201806');
通过查询方式加载数据
insert overwrite table score2 partition(month = '201806') select s_id,c_id,s_score from score1;
查询语句中创建表并加载数据
create table score2 as select * from score1;
在创建表是通过location指定加载数据的路径
create external table score6 (s_id string,c_id string,s_score int) 
row format delimited fields terminated by ',' 
location '/myscore';

export导出与import 导入 hive表数据（内部表操作）

create table techer2 like techer; --依据已有表结构创建表
export table techer to  '/export/techer';
import table techer2 from '/export/techer';


#hive表中数据导出

将查询的结果导出到本地
insert overwrite local directory '/export/servers/exporthive'
select * from score;
将查询的结果格式化导出到本地
insert overwrite local directory '/export/servers/exporthive' 
row format delimited fields terminated by '\t' 
collection items terminated by '#' 
select * from student;

将查询的结果导出到HDFS上(没有local)
insert overwrite directory '/export/servers/exporthive' 
row format delimited fields terminated by '\t' 
collection items terminated by '#' 
select * from score;

Hadoop命令导出到本地
dfs -get /export/servers/exporthive/000000_0 /export/servers/exporthive/local.txt;

hive shell 命令导出
基本语法：（hive -f/-e 执行语句或者脚本 > file）
hive -e "select * from myhive.score;" > /export/servers/exporthive/score.txt
hive -f export.sh > /export/servers/exporthive/score.txt

export导出到HDFS上
export table score to '/export/exporthive/score';

#hive的DQL查询语法

单表查询

SELECT [ALL | DISTINCT] select_expr, select_expr, ... 
FROM table_reference
[WHERE where_condition] 
[GROUP BY col_list [HAVING condition]] 
[CLUSTER BY col_list 
  | [DISTRIBUTE BY col_list] [SORT BY| ORDER BY col_list] 
] 
[LIMIT number]


注意：
1、order by 会对输入做全局排序，因此只有一个reducer，会导致当输入规模较大时，需要较长的计算时间。
2、sort by不是全局排序，其在数据进入reducer前完成排序。因此，如果用sort by进行排序，并且设置mapred.reduce.tasks>1，则sort by只保证每个reducer的输出有序，不保证全局有序。
3、distribute by(字段)根据指定的字段将数据分到不同的reducer，且分发算法是hash散列。
4、Cluster by(字段) 除了具有Distribute by的功能外，还会对该字段进行排序。因此，如果分桶和sort字段是同一个时，此时，cluster by = distribute by + sort by

WHERE语句
select * from score where s_score < 60;
GROUP BY 分组
select s_id ,avg(s_score) from score group by s_id;

分组后对数据进行筛选，使用having
select s_id ,avg(s_score) avgscore 
from score 
group by s_id 
having avgscore > 85;

如果使用 group by 分组，则 select 后面只能写分组的字段或者聚合函数where和having区别：
1 having是在group by分完组之后再对数据进行筛选，所以having 要筛选的字段只能是**分组字段**或者**聚合函数**
2 where 是从数据表中的字段直接进行的筛选的，所以不能跟在gruop by后面，也不能使用聚合函数


join 连接:
NNER JOIN 内连接：只有进行连接的两个表中都存在与连接条件相匹配的数据才会被保留下来
select * from techer t [inner] join course c on t.t_id = c.t_id; -- inner 可省略

LEFT OUTER JOIN 左外连接：左边所有数据会被返回，右边符合条件的被返回
select * from techer t left join course c on t.t_id = c.t_id; -- outer可省略

RIGHT OUTER JOIN 右外连接：右边所有数据会被返回，左边符合条件的被返回、
select * from techer t right join course c on t.t_id = c.t_id;

FULL OUTER JOIN 满外(全外)连接: 将会返回所有表中符合条件的所有记录。如果任一表的指定字段没有符合条件的值的话，那么就使用NULL值替代。
SELECT * FROM techer t FULL JOIN course c ON t.t_id = c.t_id ;

order by 排序
局排序，只会有一个reduce
ASC（ascend）: 升序（默认） DESC（descend）: 降序
SELECT * FROM students 
LEFT JOIN score sco ON s.s_id = sco.s_id 
ORDER BY sco.s_score DESC;
order by 是全局排序，所以最后只有一个reduce，也就是在一个节点执行，如果数据量太大，就会耗费较长时间

sort by 局部排序
每个MapReduce内部进行排序，对全局结果集来说不是排序。
设置reduce个数
set mapreduce.job.reduces=3;
查看设置reduce个数
set mapreduce.job.reduces;
查询成绩按照成绩降序排列
select * from score sort by s_score;
将查询结果导入到文件中（按照成绩降序排列）
insert overwrite local directory '/export/servers/hivedatas/sort' 
select * from score sort by s_score;

distribute by 分区排序
distribute by：类似MR中partition，进行分区，结合sort by使用
设置reduce的个数，将我们对应的s_id划分到对应的reduce当中去
set mapreduce.job.reduces=7;
通过distribute by  进行数据的分区
select * from score 
distribute by s_id sort by s_score;
注意：Hive要求 distribute by 语句要写在 sort by 语句之前

cluster by
当distribute by和sort by字段相同时，可以使用cluster by方式.
cluster by除了具有distribute by的功能外还兼具sort by的功能。但是排序只能是正序排序，不能指定排序规则为ASC或者DESC。
以下两种写法等价
select * from score 
cluster by s_id;

select * from score 
distribute by s_id sort by s_id;

```

## Consul
consul是hashicorp公司推出的开源工具，用于实现分布式系统的服务发现与配置。  与其它分布式服务注册与发现方案相比，consul的方案更“一站式”，  内置了服务注册与发现框架、分布一致性协议实现、健康检查、key/value存储、多数据中心方案，不再需要依赖其它工具（比如zookeeper等),使用起来也比较简单。 consul使用go语言编写，因此具有天然可移值性（支持linux,windows,mac  os); 安装包仅包仿一个可执行文件，方便部署，与docker等轻量级容器可无缝配合

**consul特性：**

1. raft算法
2. 服务发现
3. 健康检查
4. key/value存储
5. 多数据中心
6. 支持http和dns协议接口
7. 官方提供web管理办面

常见注册中心

netfix eureka

alibaba nacos

hashicorp consul

apache zookeeper

coreos etcd

cncf coredns

![image.png](../img/1674478166113267-1716728846880.png)

### 注册中心与 CAP

CAP定理：

指的是在一个分布式系统中，

Consistency（一致性）、 

Availability（可用性）、

Partition tolerance（分区容错性），三者不可同时获得

其中：

一致性（C）：所有节点都可以访问到最新的数据

可用性（A）：每个请求都是可以得到响应的，不管请求是成功还是失败

分区容错性（P）：除了全部整体网络故障，其他故障都不能导致整个系统不可用

CAP理论就是说在分布式存储系统中，最多只能实现上面的两点。

而由于当前的网络硬件肯定会出现延迟丢包等问题，所以分区容忍性是我们必须需要实现的。

所以我们只能在一致性和可用性之间进行权衡

CA： 如果不要求P（不允许分区），则C（强一致性）和A（可用性）是可以保证的。但放弃P的同时也就意味着放弃了系统的扩展性，也就是分布式节点受限，没办法部署子节点，这是违背分布式系统设计的初衷的

CP: 如果不要求A（可用），每个请求都需要在服务器之间保持强一致，而P（分区）会导致同步时间无限延长(也就是等待数据同步完才能正常访问服务)，一旦发生网络故障或者消息丢失等情况，就要牺牲用户的体验，等待所有数据全部一致了之后再让用户访问系统

AP：要高可用并允许分区，则需放弃一致性。一旦分区发生，节点之间可能会失去联系，为了高可用，每个节点只能用本地数据提供服务，而这样会导致全局数据的不一致性。

Zookeeper：CP设计，保证了一致性，集群搭建的时候，某个节点失效，则会进行选举行的leader，或者半数以上节点不可用，则无法提供服务，因此可用性没法满足

Eureka：AP原则，无主从节点，一个节点挂了，自动切换其他节点可以使用，去中心化

结论：

分布式系统中P,肯定要满足，所以只能在CA中二选一

没有最好的选择，最好的选择是根据业务场景来进行架构设计

如果要求一致性，则选择zookeeper/Nacos，如金融行业 CP

如果要求可用性，则Eureka/Nacos，如电商系统 AP

CP ： 适合支付、交易类，要求数据强一致性，宁可业务不可用，也不能出现脏数据

AP: 互联网业务，比如信息流架构，不要求数据强一致，更想要服务可用

**dev:用于开发，以下两种用于生产环境**

**client:客户端，无状态，将http和dns接口请求**转发给局域网内的服务端集群，它只是一个代理的角色。 

server:服务端 ，保存配置信息，高可用集群，每个数据中心的server数据推荐为3个或5个

![image.png](../img/1674479784507689-1716728873575.png)



上图是一个简单的consul cluster架构，consul  cluster有server和client两种角色，不管是server还是client,统称为agent,consul  client是相对无状态的，只负责转发rpc到server，资源开销很少.server是一个有一组扩展功能的代理，这些功能包括参与raft选举，维护集群状态，响应rpc查询，与其它数据中心交互wan gossip和转发查询给leader或远程数据中心。 

每个数据中心，client和server是混合的。一般建有3-5台server.这是基于有故障情况下的可用性和性能之间的权衡结果，因为越多的机器加入达成共识越慢，server之初间会选择出一个leader.**然而并不限制client的数量**，一般建议一个服务对应一个client,它们可以很容易的扩展到数千或者数万台，在开发的时候我们绑定一组服务注册中心中的客户端 即可。 

producer：服务提供者

consumer:服务消费者



![image.png](../img/1674480519991279-1716728873575.png)

服务发现及注册：

producer启动时，会将自己的ip/host等信息通过发送请求告知consul,consul接收到producer的注册信息后，每隔10秒（默认）会向producer发送一个健康检查的请求，检查producer是否处于可用状态，防止consumer调到不可用的服务；

服务调用

当consumer请求product时，会先从consul中拿存储的producer服务的ip和port的临时表（temp  table),从表中任选一个producer的ip和port,然后根据这个ip和port,发送访问请求;此表只包含通过健康检查的producer信息，并且每隔10秒更新。。

## 时序数据库

（提纲占位，待补充具体产品与实践笔记。）

## 向量数据库

（提纲占位，待补充 Qdrant 等专题；见 [7-qdrant.md](7-qdrant.md)。）

## 消息中间件

### Kafka

作用：

异步、削峰、[解耦](https://so.csdn.net/so/search?q=解耦&spm=1001.2101.3001.7020)

消息队列两种模式：

1： 点对点模型

消费者主动拉取数据，消息收到后清除消息

<img src="../img/image-20231010214906987.png" alt="image-20231010214906987" style="zoom:50%;" />

2： 发布订阅模式

1. 可以有多个topic 主题
2. 消费者消费数据后，不删除数据
3. 每个消费者相互独立，都可以消费到数据

同步的概念：

![image-20231010215755388](../img/image-20231010215755388-1716730906768.png)

*用户发起一个请求，系统A收到请求，接着系统A必须立马去调用系统B，直到系统B返回了，系统A
 `才能`返回结果给用户*

中间件实现异步：

![image-20231010215830614](../img/image-20231010215830614-1716730906770.png)

![image-20231010215930496](../img/image-20231010215930496-1716730906770.png)





 Kafka是一个分布式发布 - 订阅消息系统和一个强大的队列

Kafka可以在许多用例中使用。 其中一些列出如下 - 

- **指标**  -  Kafka通常用于操作监控数据。 这涉及聚合来自分布式应用程序的统计信息，以产生操作数据的集中馈送。
- **日志聚合解决方案**  -  Kafka可用于跨组织从多个服务收集日志，并使它们以标准格式提供给多个服务器。
- **流处理**  - 流行的框架(如Storm和Spark Streaming)从主题中读取数据，对其进行处理，并将处理后的数据写入新主题，供用户和应用程序使用。 Kafka的强耐久性在流处理的上下文中也非常有用。

Topic ： 主题

Partition： 分区

Partiion offset  分区偏移

Brokers

Producers

Consumers 

Leader

Follower

![image-20231010221119385](../img/image-20231010221119385-1716730906770.png)

100T 数据 ->producer ->topic(单台机器存储空间不够，partition ) 

kafka cluster 集群 ：  leader 和follower 

注意： 每个组内的消费者，只能单独消费1个parttion 

zookpper : 可以有，可以没有

```
基本操作：
create topic 
list topic 
create producer 
create consumer (从当前开始消费，或者从头开始)


```
#### producer

生产者发送数据：

RecordAccumulator: 是缓存队列

sender 线程： 什么时候拉取数据 ， batch_size  , linger.ms



![image-20231010222637375](../img/image-20231010222637375-1716730906770.png)

**异步发送：**

send  or 带callback 的send 

同步发送：

分区器的好处：

<img src="./img/image-20231011202409976.png" alt="image-20231011202409976" style="zoom:50%;" />

**分区策略：send 方法**
the default partitioning strategy：

1. if a parttion is specific in the record ,use it 
2. if no parttion is specific but a key is present choose a partition based on the hash of the key 
3. if no parttion or key is present choose the sticky partition that changes when the batch is full

![image-20231011203245028](../img/image-20231011203245028-1716730906770.png)

**自定义分区器：**

需求： 实现一个分区器： 当发送过来的数据包含 test_partition , 就发送到0 号分区，否则就发送到其他分区

实现步骤： 

（1）定义类实现partitioner 接口

（2）重写parttion()方法

**生产者如何提高吞吐量：**

batch.size 16k ->32K

linger.ms 5-100ms

RecordAccumulator: 缓冲器大小，修改为64m

<img src=".img/image-20231011204122128.png" alt="image-20231011204122128" style="zoom:50%;" />



**数据可靠性：**

acks 应答：

![image-20231011204432879](../img/image-20231011204432879-1716730906770.png)



in-sync replica set(ISR):

![image-20231011204956013](../img/image-20231011204956013-1716730906771.png)

数据完全可靠条件： ack =-1 分区副本数>=2 , isr 里应答的最小副本数量>=2 

isr: 是集群所有的broker 节点

数据重复： ack =-1  当leader 节点接受到数据，挂掉，但是没有同步到producer,但是已经同步给了follwer,  新选的leader , 又接受相同的数据，就重复了

![image-20231011205252718](../img/image-20231011205252718-1716730906771.png)

**数据的传递语义：**

At Least Once : 至少一次

At most once : 最多一次

Exactly Once : 精确一次

<img src="../img/image-20231011205734232.png" alt="image-20231011205734232" style="zoom:50%;" />

![image-20231011210132550](../img/image-20231011210132550-1716730906771.png)



不想数据重复，必须开启事务

![image-20231011210713487](../img/image-20231011210713487-1716730906771.png)

![image-20231011210846592](../img/image-20231011210846592-1716730906771.png)

**数据有序：**

![image-20231011211301535](../img/image-20231011211301535-1716730906771.png)



一个分区： 就能保住有序 

否则，一个消费者，拉取所有分区数据再排序

**数据乱序：**

![image-20231011211422176](../img/image-20231011211422176-1716730906771.png)

![image-20231011211741270](../img/image-20231011211741270-1716730906771.png)



**zookeeper**

![image-20231011212030240](../img/image-20231011212030240-1716730906771.png)

![image-20231011212154020](../img/image-20231011212154020-1716730906771.png)



![image-20231011212250632](../img/image-20231011212250632-1716730906771.png)

![image-20231011212608107](../img/image-20231011212608107-1716730906771.png)

![image-20231011212646079](../img/image-20231011212646079-1716730906772.png)

![image-20231011212717335](../img/image-20231011212717335-1716730906772.png)

<img src="../img/image-20231011212908145.png" alt="image-20231011212908145" style="zoom:50%;" />

![image-20231011212933978](../img/image-20231011212933978-1716730906772.png)



#### kafka 副本

![image-20231011213033142](../img/image-20231011213033142-1716730906772.png)



![image-20231011213312430](../img/image-20231011213312430-1716730906772.png)

![image-20231011213418001](../img/image-20231011213418001-1716730906772.png)



![image-20231011213539712](../img/image-20231011213539712-1716730906772.png)

负载均衡：均匀分布

![image-20231011213840436](../img/image-20231011213840436-1716730906772.png)



**手动调整分区副本存储：**

![image-20231011214039473](../img/image-20231011214039473-1716730906772.png)

![image-20231011214220540](../img/image-20231011214220540-1716730906772.png)

![image-20231011214346339](../img/image-20231011214346339-1716730906772.png)

#### 文件存储

![image-20231011214411747](../img/image-20231011214411747-1716730906772.png)

切割： topic -> parttion ->log->segement ->()

分片+索引

![image-20231011215027126](../img/image-20231011215027126-1716730906772.png)

删除策略： delete 和compact 两种：

![image-20231011215709797](../img/image-20231011215709797-1716730906772.png)



#### kafka 高效率读写数据

![image-20231011220139633](../img/image-20231011220139633-1716730906773.png)

![image-20231011220346557](../img/image-20231011220346557-1716730906773.png)

![image-20231011220433663](../img/image-20231011220433663-1716730906773.png)

4： 页缓存+ 0拷贝技术

#### consumer

![image-20231011220838811](../img/image-20231011220838811-1716730906773.png)

拉： 是consumer 主动

推： 是producer 主动

**消费流程**：

![image-20231011221814778](../img/image-20231011221814778-1716730906773.png)

消费者之间是相互独立的

offset 持久化保存

![image-20231011221936943](../img/image-20231011221936943-1716730906773.png)

1个消费者： 也需要提供一个消费者组id 

![image-20231011222204643](../img/image-20231011222204643-1716730906773.png)

![image-20231011222315193](../img/image-20231011222315193-1716730906773.png)



![image-20231011222515078](../img/image-20231011222515078-1716730906773.png)

create consumer 

subscribe  订阅topic

assgin 订阅某个topoic 下的某个分区

![image-20231011223254517](../img/image-20231011223254517-1716730906773.png)

组内怎么分配分区：

![image-20231011223431910](../img/image-20231011223431910-1716730906773.png)

分区数只能增加不能减少

![image-20231011223629129](../img/image-20231011223629129-1716730906773.png)

![image-20231011223658173](../img/image-20231011223658173-1716730906773.png)



offset **维护位置**

![image-20231011223849468](../img/image-20231011223849468-1716730906773.png)



![image-20231011224043531](../img/image-20231011224043531-1716730906774.png)



![image-20231011224230890](../img/image-20231011224230890-1716730906774.png)



offset 消费

![image-20231011224336632](../img/image-20231011224336632-1716730906774.png)



1. 指定位置进行消费： 指定offset 进行消费

2. 指定时间消费：在生成环境中，会遇到最近消费的几个小时数据异常，想要新按照时间消费。

   把时间转成对应的offset  :

**漏消费**：

**重复消费**：

![image-20231012204951962](../img/image-20231012204951962-1716730906774.png)

![image-20231012205117742](../img/image-20231012205117742-1716730906774.png)

**消息积压**：

![image-20231012205244371](../img/image-20231012205244371-1716730906774.png)



![image-20231012205458065](../img/image-20231012205458065-1716730906774.png)

![image-20231012205530621](../img/image-20231012205530621-1716730906774.png)



![image-20231012205612628](../img/image-20231012205612628-1716730906774.png)



![image-20231012205718244](../img/image-20231012205718244-1716730906774.png)



![image-20231012205931865](../img/image-20231012205931865-1716730906774.png)

![image-20231012210001842](../img/image-20231012210001842-1716730906774.png)

![image-20231012210033527](../img/image-20231012210033527-1716730906774.png)





https://www.bilibili.com/video/BV1vr4y1677k?p=10&spm_id_from=pageDriver&vd_source=ae11379595599a1cedeb268c109fc9bb

https://achang.blog.csdn.net/article/details/121307740



优先队列的实现：

![image-20231012213008856](../img/image-20231012213008856-1716730906774.png)

https://blog.csdn.net/GaleZhang/article/details/126493027

### RabbitMQ

4大核心

1. 生产者
2. 消费者
3. 队列
4. 交换机

**生产者**：产生数据发送消息的程序是生产者。

**交换机**：交换机是 RabbitMQ 非常重要的一个部件，一方面它接收来自生产者的消息，另一方面它将消息推送到队列中。交换机必须确切知道如何处理它接收到的消息，是将这些消息推送到特定队列还是推送到多个队列，亦或者是把消息丢弃，这个是由交换机类型决定的。

**队列**：队列是 RabbitMQ 内部使用的一种数据结构，尽管消息流经 RabbitMQ  和应用程序，但它们只能存储在队列中。队列仅受主机的内存和磁盘限制的约束，本质上是一个大的消息缓冲区。许多生产者可以将消息发送到一个队列，许多消费者可以尝试从一个队列接收数据。

**消费者**：消费与接收具有相似的含义。消费者大多时候是一个等待接收消息的程序。请注意生产者，消费者和消息中间件很多时候并不在同一机器上。同一个应用程序既可以是生产者又是可以是消费者。

AMQP 协议是一种二进制协议， 它定义了一组规则和标注，以确保消息可以在不同的应用程序和平台传递和解释，AMQP 协议包含4个核心组件

- 消息
- 交换机
- 队列
- 绑定

![image-20231225212920034](../img/image-20231225212920034.png)



- `Broker`：就是 RabbitMQ 服务，用于接收和分发消息，接受客户端的连接，实现 AMQP 实体服务。
- `Virtual host`：出于多租户和安全因素设计的，把 AMQP 的基本组件划分到一个虚拟的分组中，类似于网络中的 namespace 概念。当多个不同的用户使用同一个 RabbitMQ server 提供的服务时，可以划分出多个 vhost，每个用户在自己的 vhost 创建 exchange 或 queue 等。
- `Connection`：连接，生产者/消费者与 Broker 之间的 TCP 网络连接。
- `Channel`：网络信道，如果每一次访问 RabbitMQ 都建立一个 Connection，在消息量大的时候建立连接的开销将是巨大的，效率也较低。Channel 是在 connection 内部建立的逻辑连接，如果应用程序支持多线程，通常每个 thread 创建单独的 channel 进行通讯，AMQP method 包含了 channel id 帮助客户端和 message broker 识别 channel，所以 channel  之间是完全隔离的。Channel 作为轻量级的Connection 极大减少了操作系统建立 TCP connection 的开销。
- `Message`：消息，服务与应用程序之间传送的数据，由Properties和body组成，Properties可是对消息进行修饰，比如消息的优先级，延迟等高级特性，Body则就是消息体的内容。
- `Virtual Host`：虚拟节点，用于进行逻辑隔离，最上层的消息路由，一个虚拟主机理由可以有若干个Exhange和Queue，同一个虚拟主机里面不能有相同名字的Exchange

- `Exchange`：交换机，是 message 到达 broker 的第一站，用于根据分发规则、匹配查询表中的 routing key，分发消息到 queue 中去，不具备消息存储的功能。常用的类型有：direct、topic、fanout。
- `Bindings`：exchange 和 queue 之间的虚拟连接，binding 中可以包含 routing key，Binding 信息被保存到 exchange 中的查询表中，用于 message 的分发依据。
- `Routing key`：是一个路由规则，虚拟机可以用它来确定如何路由一个特定消息
- `Queue`：消息队列，保存消息并将它们转发给消费者进行消费。

![image-20231225214036775](../img/image-20231225214036775.png)



fanout

Direcot



### RocketMQ

RocketMQ是阿里开源的消息中间件，久经沙场，非常的靠谱。他几乎同时解决了Kafka和RabbitMQ的缺陷。



### nginx

![image-20240118210735429](../img/image-20240118210735429-1716730906775.png)



![image-20240118210833942](../img/image-20240118210833942-1716730906775.png)



![image-20240118210921650](../img/image-20240118210921650-1716730906775.png)



nginx -v :

查看支持的模块：

nginx -s reload  会发什么？

worker 会变， master 不会变

nginx -s stop

rpm -ql nginx  # 查看nginx 配置文件

![image-20240118212114272](../img/image-20240118212114272-1716730906775.png)

server ： 虚拟主机，必须写在http {} 区域中。

![image-20240118212402782](../img/image-20240118212402782-1716730906775.png)

单虚拟主机：

基于多ip的虚拟主机

多域名的虚拟主机：

![image-20240118214915689](../img/image-20240118214915689-1716730906775.png)







```
server {
    listen 80; # 如果需要HTTPS，请替换为listen 443 ssl，并配置SSL证书相关项
    server_name dockerhub.kubekey.local;

    location / {
        proxy_pass http://127.0.0.1:4433;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}


server {
    listen 443 ssl;
    server_name dockerhub.kubekey.local;

    # SSL证书配置部分
    ssl_certificate /etc/docker/certs.d/dockerhub.kubekey.local/dockerhub.kubekey.local.cert;
    ssl_certificate_key /etc/docker/certs.d/dockerhub.kubekey.local/dockerhub.kubekey.local.key;

    location / {
        proxy_pass https://192.168.5.24:4433;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

```
## 负载均衡中间件

Nginx

LVS 

KeepLive 

CDN 

## RPC

grpc : google 开源的高性能 rpc 框架，stubby  演化

1. 网络通信 （grpc 自己封装网络通信部分，C，java[Netty] ,Go）
2. 协议  http2  传输数据的时候，二进制内容 支持双向流 双工，连接的多路复用
3. 序列化  基本文本， json , 二进制， Thrift 二进制序列化， 压缩二进制序列化 protobuf google 开源的一种序列化（IDL 语言）
4. 代理的创建  让调用者像调用本地方法那样，去调用远端的服务方法

thrift 与gRPC 的区别：

共性： 支持异构语言的RPC

区别：

1. 网络通信： thrift TCP  专属协议   gPRC  http2
2. 性能角度：  thrift 效率 高于gprc

grpc 好处：

1. 高效的进程间通信
2. 支持多种语言， C，GO， Java 
3. 支持多平台 linux
4. grpc protobuf 效率高
5. http2 协议
6. 大厂背书

### HTTP

http1.0  协议 ：  请求响应模式， 短连接协议 （无状态协议），单工 无法实现服务器推送

变现轮询，（客服端轮询，隔一段时间就发送请求），增加服务器压力

http1.1 协议： 请求响应模式，有限的长连接，升级的方式websocket , 双工，实现服务器向客服端的推送

1. 传输数据文本格式，可读性好，效率差
2. 本质http1.x 协议无法实现双工通信
3. 资源的请求，需要发送多次请求，建立多个连接才可以完成

http 是基于TCP 长连接， 但是服务器压力大，主动断开

htt2.0 协议：

1. 是一个二进制协议，
2. 双工通信
3. 多路复用
4. 流控。数据流优先级

RPC ： remote procedure call

![image-20240111213716628](../img/image-20240111213716628-1716730962437.png)

![image-20240111213909909](../img/image-20240111213909909-1716730962438.png)

![image-20240111213953081](../img/image-20240111213953081-1716730962438.png)

![image-20240111214113129](../img/image-20240111214113129-1716730962438.png)

![image-20240111214147087](../img/image-20240111214147087-1716730962438.png)

![image-20240111214558971](../img/image-20240111214558971-1716730962438.png)

![image-20240111214621301](../img/image-20240111214621301-1716730962438.png)

![image-20240117205421686](../img/image-20240117205421686-1716730962438.png)



![image-20240117205615666](../img/image-20240117205615666-1716730962438.png)

![image-20240117205727832](../img/image-20240117205727832-1716730962438.png)

![image-20240117205924877](../img/image-20240117205924877-1716730962438.png)

![image-20240117205950751](../img/image-20240117205950751-1716730962438.png)



![image-20240117210036671](../img/image-20240117210036671-1716730962438.png)







