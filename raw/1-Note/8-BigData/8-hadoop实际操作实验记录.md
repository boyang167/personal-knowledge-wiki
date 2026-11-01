hadoop实际操作实验记录

## 1： 安装centos7

~~~
配置静态IP
ip addr
vi /etc/sysconfig/network-scripts/ifcfg-ens33
BOOTPROTO=static静态IP地址
ONBOOT=yes 开机使用配置
PADDR=192.168.100.95（IP地址）
NETMASK=255.255.255.0（子网掩码）
GATEWAY=192.168.100.254（网关）
DNS1=8.8.8.8（首选DNS）
# 虚拟机的设置
https://blog.csdn.net/YeMaZhi/article/details/105043073
~~~

## 2：安装java 环境

~~~
tar -xzvf jdk-8u241-linux-x64.tar.gz
mv jdk-8u241-linux-x64 jdk1.8.0
vi /etc/profile
export JAVA_HOME=/home/hadoop/softs/jdk1.8.0  # 修改这个路径
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
source /etc/profile
# 查看java jdk 是否安装成功 
which java
java -version 
~~~

## 3: 安装mysql

~~~
https://blog.csdn.net/weixin_43451430/article/details/115553108

yum update -y
sudo yum install -y wget 
wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
sudo yum localinstall mysql80-community-release-el7-3.noarch.rpm -y
sudo yum install -y yum-utils
yum repolist enabled | grep "mysql.*-community.*"
yum repolist all | grep mysql

关闭MySQL8.0
sudo yum-config-manager --disable mysql80-community
开启MySQL5.7
sudo yum-config-manager --enable mysql57-community

yum repolist enabled | grep mysql
#安装MySQL
sudo yum install -y mysql-community-server
# 出现问题
yum module disable mysql
sudo yum install -y mysql-community-server
如果保存gpk  编辑文件
/etc/yum.repos.d/mysql-community.repo 
gpgcheck=0

启动MySQL
sudo service mysqld start
查看MySQL服务状态
sudo service mysqld status
初始化MySQL
sudo grep 'temporary password' /var/log/mysqld.log  # 查看密码
mysql -u root -p

初始化密码
ALTER USER 'root'@'localhost' IDENTIFIED BY 'Asdf!123456';

SHOW VARIABLES LIKE 'validate_password%'; 
#修改密码验证强度
set global validate_password_policy=LOW; 
set global validate_password_length=6;
#设置MySQL远程连接，在sql里面设置
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
FLUSH PRIVILEGES;

systemctl enable mysqld
#MySQL的配置文件目录：
/etc/my.cnf
#配置防火墙
firewall-cmd --zone=public --add-port=3306/tcp --permanent

测试mysql 是否连通
yum-y install telnet
    1:telnet host port
    2:mysql -h ip -uroot -ppwd
    
如果写入是乱码
查看数据库和表的编码 

~~~



## 4： SHH

~~~
查看是否安装 
rpm -qa | grep ssh
ssh clinet
ssh server
# 安装 
sudo yum install openssh-clients
sudo yum install openssh-server
# 测试 
ssh localhost  
exit  退出ssh 连接

ssh 无密码登录 
# ssh-keygen 生成秘钥  
cd ~/.ssh/         # 若没有该目录，请先执行一次ssh localhost
ssh-keygen -t rsa   # 回车
cat id_rsa.pub >> authorized_keys  # 加入授权
chmod 600 ./authorized_keys    # 修改文件权限
~~~

## 5:安装 anaconda 

~~~
https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/  # 清华大学开源空间

# 下载
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2021.05-Linux-x86_64.sh
# 安装
bash Anaconda3-2021.05-Linux-x86_64.sh
export anacoda_path=$PATH:/root/anaconda3/bin:$PATH
export -p

conda -V
conda init
conda config --set auto_activate_base false  # 不执行 conda 环境

conda info -e  # 查看所有虚拟环境
conda create -n env_name python=3.6
conda activate env_name
conda deactivate  env_name
conda list
conda remove --name env_name --all

conda env export 0n env_name >env.yml #导出环境到yml文件
conda env create -f env.yml  #根据yml文件创建环境


查看当前的环境变量：conda env config vars list
设置环境变量：conda env config vars set my_var=value
取消环境变量：conda env config vars unset my_var

# 源
conda config --show
conda config --get channels

#添加
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/main/
#Conda Forge
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/conda-forge/
#pytorch
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/pytorch/

#删除
conda config --remove channels CHANNEL
conda config --remove channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/free/

~~~

###  install jupyter notebook

~~~
conda install jupyter notebook
# 产生配置文件
jupyter notebook --generate-config
终端输入python:
from notebook.auth import passwd
passwd()
#设置密码 123456
'argon2:$argon2id$v=19$m=10240,t=10,p=8$ZzueEBxeIuJ3Uyf4Nolv5Q$CgYmdQqXn0RvLgCrVPS84Q'

# 在产生的配置文件中添加如下信息 
c.NotebookApp.ip='*'                     # 就是设置所有ip皆可访问  
c.NotebookApp.password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$ZzueEBxeIuJ3Uyf4Nolv5Q$CgYmdQqXn0RvLgCrVPS84Q'    # 上面复制的那个sha密文'  
c.NotebookApp.open_browser = False       # 禁止自动打开浏览器  
c.NotebookApp.port =8888                 # 端口
c.NotebookApp.notebook_dir = '/home/jupyter_datas'  #设置Notebook启动进入的目录

systemctl stop firewalld.service
jupyter notebook --allow-root
conda install nb_conda_kernels
~~~



## 6：hadoop 

~~~
百度网盘 林子
http://dblab.xmu.edu.cn/blog/2441-2/

useradd -m hadoop -s /bin/bash   # 创建新用户hadoop
passwd hadoop  #修改密码
visudo   # 将hadoop 用户进行提权
hadoop ALL=(ALL) ALL

# hadoop伪分布式配置 
export HADOOP_HOME=/home/hadoop/softs/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
伪分布式需要修改2个配置文件 core-site.xml 和 hdfs-site.xml 
./etc/hadoop 文件夹中

core-site.xml
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>file:/usr/local/hadoop/tmp</value>
        <description>Abase for other temporary directories.</description>
    </property>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>

hdfs-site.xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:/usr/local/hadoop/tmp/dfs/name</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:/usr/local/hadoop/tmp/dfs/data</value>
    </property>
</configuration>

配置完成后，执行 NameNode 的格式化:
./bin/hdfs namenode -format
./sbin/start-dfs.sh


./sbin/start-dfs.sh
出现错误 
but there is no HDFS_NAMENODE_USER defined. Aborting operation.

start-dfs.sh和stop-dfs.sh添加下列参数
HDFS_DATANODE_USER=root
HADOOP_SECURE_DN_USER=hdfs
HDFS_NAMENODE_USER=root
HDFS_SECONDARYNAMENODE_USER=root

start-yarn.sh和stop-yarn.sh文件，添加下列参数
#!/usr/bin/env bash
YARN_RESOURCEMANAGER_USER=root
HADOOP_SECURE_DN_USER=yarn
YARN_NODEMANAGER_USER=root
出现错误 
localhost: ERROR: JAVA_HOME is not set and could not be found.
vi ./etc/hadoop/hadoop-env.sh
 添加
 export JAVA_HOME=/home/hadoop/softs/jdk1.8.0
 
 
# 配置yarm
mapred-site.xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>

yarn-site.xml
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
        </property>
</configuration>
然后就可以启动 YARN 了（需要先执行过 ./sbin/start-dfs.sh）
./sbin/start-yarn.sh      $ 启动YARN
./sbin/mr-jobhistory-daemon.sh start historyserver  # 开启历史服务器，才能在Web中查看任务运行情况
~~~

#### hadoop的使用

~~~~
hdfs dfs -mkdir -p /user/hadoop  #创建文件夹
hdfs dfs -put local_path_file hdfs_path # 上传到hdfs 文件系统中
hdfs dfs -get hdfs_path_file local_path # 下载到本地
# 关闭防火墙
systemctl stop firewalld.service
~~~~

## 6: Hbase

~~~
https://dblab.xmu.edu.cn/blog/2442-2/
单机模式配置
~~~

## 7： hive

~~~
# 要把jdbc 复制到hive/lib 
mysql-connector-java-5.1.40/mysql-connector-java-5.1.40-bin.jar 
./bin/schematool -dbType mysql -initSchema
$ vi hive-site.xml
    <property>
        <name>javax.jdo.option.ConnectionDriverName</name>
        <value>com.mysql.cj.jdbc.Driver</value>
    </property>
修改为
    <property>
        <name>javax.jdo.option.ConnectionDriverName</name>
        <value>com.mysql.jdbc.Driver</value>
    </property>
    
    
hadoop-3.2.1（路径：hadoop\share\hadoop\common\lib）中该jar包为  guava-27.0-jre.jar；而hive-3.1.2(路径
~~~

### hive的基本操作

~~~
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
~~~



## 8：spark

~~~
cp ./conf/spark-env.sh.template ./conf/spark-env.sh
export SPARK_DIST_CLASSPATH=$(/home/hadoop/softs/hadoop/bin/hadoop classpath)

export SPARK_HOME=/home/hadoop/softs/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME


# 安装pyspark
pip install -U -i https://pypi.tuna.tsinghua.edu.cn/simple pyspark
pip install pyspark -i https://pypi.doubanio.com/simple/

export SPARK_HOME=/home/hadoop/softs/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME

export PYSPARK_PYTHON=/root/anaconda3/bin/python
export PYSPARK_DRIVER_PYTHON=/root/anaconda3/bin/python

~~~

### 基本使用

#### RDD:

~~~
							key 		 v 		
rdd2 =rdd1.map(lambda v: (v.genre, int(v.num_of_sales))).reduceByKey(lambda x, y: x + y).collect()  # collect 返回的是 []
json.dumps(rdd2)
# 注意reducebykey  x,y : x+y    都是 value 

# 两个列求和 
					 key						v-> []
rdd.map(lambda v: (int(v.year_of_pub),  [ int(v.num_of_tracks), 1] ))\
.reduceByKey(lambda x, y: [x[0] + y[0], x[1] + y[1]]).sortByKey()
 = res = [k ,v]
list(map(lambda v: v[0], result))
list(map(lambda v: v[1][0], result))
list(map(lambda v: v[1][1], result))

						 key ()  元组								v 				
rdd.map(lambda v: ( (v.genre, int(v.year_of_pub)), int(v.num_of_sales)))\
.reduceByKey(lambda x, y: x + y).sortByKey().collect()

#多列 聚合操作  
rdd.map(lambda v: (v.genre, (float(v.rolling_stone_critic), float(v.mtv_critic), float(v.music_maniac_critic), 1)))\
.reduceByKey(lambda x, y : (x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3]))\
.map(lambda v: (v[0], v[1][0]/v[1][3], v[1][1]/v[1][3], v[1][2]/v[1][3])).collect()

~~~

#### spark sql :

~~~python
import pyspark.sql.functions as f
f.split(df['categories'], ',') # f
1: withColumn()
使用带有列的PySpark更改列DataType df.withColumn(x, df[x].cast('int'))
更新现有列的值  df.withColumn( "newDate",split(df['Date'], " ")[0] ).drop("Date")
从现有的创建新列
2:重命名列名
df.withColumnRenamed()  df = df.withColumnRenamed('old_name','new_name')
df.drop()
# 创建临时表
3df.createOrReplaceTempView('table_name')

4:explode 将列数据展开
[a,b,[1,2]]
[a,b,1]
[a,b,2]

5：from pyspark.sql.functions import regexp_replace
df.withColumn('address', regexp_replace('address', 'Rd', 'Road')) \
  .show(truncate=False)
6： 写在本地
df.write.parquet("file:///home/hadoop/wangyingmin/yelp-etl/business_etl", mode="overwrite")
df.write.json(path, model)
df = spark.read.parquet(data_path).cache()

def read_json(file_path):
    json_path_names = os.listdir(file_path)
    data = []
    for idx in range(len(json_path_names)):
        json_path = file_path + '/' + json_path_names[idx]
        if json_path.endswith('.json'):
            with open(json_path) as f:
                for line in f:
                    data.append(json.loads(line))
    return data
df = read_json(path)

# 读取json 文件 dataframe
spark.read.csv("input/earthquake_cleaned.csv",  header=True, inferSchema=True)
df.toPandas().to_csv("earthquakeC.csv", encoding='utf-8', index=False)
df.groupBy("Year").count().orderBy("Year")
# 过滤
df.filter("Area is not null")
#排序
df.sort(df["Magnitude"].desc(), df["Year"].desc()).take(500)
#当震源深度相同时，将震级更高的地震排在前面。
df.sort( df["Depth"].desc(), df["Magnitude"].desc() ).take(500)
# 取别名 alias
rawData.agg(*[count(c).alias(c) for c in rawData.columns]).show()

df['y'] # 取值 [0,1]
df_age = df.select(df['age'],df['y'])
bin = [0,30,45,60,75,100]
# 统计各个年龄段 0的人数
df_age.filter(df['age'].between(bin[i],bin[i+1])).filter(df['y']=='0').count()


# 月收入分析
df_income = df.select(df['MonthlyIncome'],df['y'])
# 获取平均值，其中先返回Row对象，再获取其中均值
mean_income = df_income.agg(functions.avg(df_income['MonthlyIncome'])).head()[0]
# 收入分布，105854人没超过均值6670，44146人超过均值6670
df_income.filter(df['MonthlyIncome'] < mean_income).count()

df.select("Job").distinct().show(truncate=False)
df.dropDuplicates((['Job'])).select("Job").show(truncate=False)
~~~



#### dataframe:

~~~python
fields = [ StructField("date", DateType(),False),StructField("county", StringType(),False),StructField("deaths", IntegerType(),False),]  # false 不能为空
schema = StructType(fields)

# flagMap  对集合中每个元素操作  ，在扁平化  [ [a,b],[a,d]] -> [a ,b,a,d]
# map    对集合中每个元素操作  [ [a,b],[a,d]] -> [[a,b],[a,d]]
df.select(field).filter(mdf[field] != '').rdd.flatMap(lambda g: [(v, 1) for v in map(lambda x: x['name'], json.loads(g[field]))])

df = df.filter(df.price != '面议').withColumn("price",df.price.cast(IntegerType()))

# 对多列进行不同的聚合操作, 并修改相应的列名
df.groupBy('job').agg(
    F.sum("salary").alias("sum_salary"),
    F.avg("salary").alias("avg_salary"),
    F.min("salary").alias("min_salary"),
    F.max("salary").alias("max_salary"),
    F.mean("salary").alias("mean_salary")
).show(truncate=False)      # truncate=False：左对齐

df.agg(F.sum("rain1h").alias("rain24h")).sort(F.desc("rain24h")

df_rain_sum.coalesce(1).write.csv("file:///home/analyse.csv")
df = spark.read.csv(filename,header = True)

F.date_format(df['time'],"yyyy-MM-dd").alias("date")
F.hour(df['time']).alias("hour")

                                              
df.filter(df['hour'].isin([2,8,12,20]))
                                              
F.format_number('avg_temperature',1)                                            

~~~

