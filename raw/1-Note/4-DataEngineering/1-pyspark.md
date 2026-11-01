# PySpark 笔记

## 目录

- [基础与数据源](#基础与数据源)
- [RDD](#rdd)
- [Spark SQL / DataFrame](#spark-sql--dataframe)
- [Spark 新特性（AQE）](#spark-新特性aqe)
- [Spark Core 补充](#spark-core补充)
- [参考链接](#参考链接)

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("template").getOrCreate()

# 惰性求值：Transformation 链在 Action 前不会执行
df = df.filter(col("age") > 30)
df = df.groupBy("key").count()
df = df.select("name", "age")
```

## 基础与数据源

![1750768790821](../img/1750768790821.png)

![1750768823691](../img/1750768823691.png)

![1750768906866](../img/1750768906866.png)

![1750768966608](../img/1750768966608.png)

![1750770907056](../img/1750770907056.png)

Spark 常见数据源：

| 类型 | 示例 |
| --- | --- |
| 文件 / 表 | localFS、HDFS、Hive；text、Parquet、ORC、JSON、CSV |
| 关系库 | MySQL、Oracle 等 JDBC |
| NoSQL | HBase、Elasticsearch、Redis |
| 消息 | Kafka |

![1750771190074](../img/1750771190074.png)

![1750771219920](../img/1750771219920.png)

![1750773133412](../img/1750773133412.png)

![1750773185955](../img/1750773185955.png)

![1750773394169](../img/1750773394169.png)

![1750773735399](../img/1750773735399.png)

![1750774312244](../img/1750774312244.png)

### Spark on YARN

![1750774620586](../img/1750774620586.png)

![1750774755369](../img/1750774755369.png)

![1750774836459](../img/1750774836459.png)

![1750774905415](../img/1750774905415.png)

![1750775013752](../img/1750775013752.png)

![1750775058673](../img/1750775058673.png)

![1750775564768](../img/1750775564768.png)

![1750857839417](../img/1750857839417.png)

![1750857857236](../img/1750857857236.png)

![1750857973781](../img/1750857973781.png)

## RDD

![1750858252110](../img/1750858252110.png)

![1750858352570](../img/1750858352570.png)

![1750858591471](../img/1750858591471.png)

![1750860000171](../img/1750860000171.png)

![1750860042262](../img/1750860042262.png)

![1750860087355](../img/1750860087355.png)

![1750860126153](../img/1750860126153.png)

![1750860857461](../img/1750860857461.png)

### **`groupBy` 的使用**

`groupBy` 是一个通用的分组方法，可以按照指定的条件对 RDD 或 DataFrame 进行分组，通常结合聚合函数（如 `sum`, `count`, `avg` 等）使用。

`groupByKey` 是专门用于 `(key, value)` 键值对 RDD 的分组操作，直接按照 key 分组，不需要额外指定分组条件。

1. **`groupBy` 和 `groupByKey` 都会触发 shuffle** ，可能影响性能，尽量结合 `reduceByKey` 或 `aggregateByKey` 使用。
2. **分组后数据可能倾斜** （某些 key 数据过多），可以考虑 `repartition` 或使用 `combineByKey` 优化。

Transformation:

1. **join()** : 只返回两个RDD中键匹配的元素
2. **leftOuterJoin()** : 返回左RDD所有元素，右RDD无匹配则为None
3. **rightOuterJoin()** : 返回右RDD所有元素，左RDD无匹配则为None
4. **intersection()** : 返回两个RDD中都存在的完全相同的元素
5. **glom**：按分区返回数组
6. **groupBy**
7. **groupByKey**
8. reduceByKey
9. sortBy 如果全局有序，排序分区数请设置为1
10. sortByKey

Action :

1. countByKey()
2. collect 将RDD 各个分区数据拉到driver
3. reduce
4. fold  初始值
5. first
6. takeSample
7. takeOrdered
8. foreach
9. saveAsTextFile

分区操作算子

`mapPartitions` 是对每个分区进行操作，而不是对每个元素操作。它接收一个分区的所有数据作为输入(Iterator)，并返回一个输出(Iterator)。

foreachPartition

| 特性         | mapPartitions      | foreachPartition   |
| ------------ | ------------------ | ------------------ |
| 返回值       | 返回新的RDD        | 不返回任何值       |
| 用途         | 转换操作           | 行动操作           |
| 资源初始化   | 每个分区初始化一次 | 每个分区初始化一次 |
| 性能         | 比map高效          | 比foreach高效      |
| 典型应用场景 | 数据转换、过滤     | 数据写入外部系统   |

**partitionBy**、**repartition**；**groupByKey** 与 **reduceByKey**（后者通常更少 shuffle）：

![1750944367991](../img/1750944367991.png)

![1750944387208](../img/1750944387208.png)

RDD 的数据是过程的数据

![1750944588369](../img/1750944588369.png)

![1750944644694](../img/1750944644694.png)

![1750944716729](../img/1750944716729.png)

![1750944750761](../img/1750944750761.png)

## Spark SQL / DataFrame

![1751108705760](../img/1751108705760.png)

![1751108776687](../img/1751108776687.png)

![1751108814396](../img/1751108814396.png)

![1751108873681](../img/1751108873681.png)

![1751108907207](../img/1751108907207.png)

![1751118006526](../img/1751118006526.png)

![1751118102649](../img/1751118102649.png)

![1751118209924](../img/1751118209924.png)

### DataFrame 与 Schema

- **StructType / StructField**：列类型与可空性  
- **Row**：行；**Column**：列  
- `spark.createDataFrame(...)`、`df.printSchema()`  
- `df.createOrReplaceTempView("t")`：注册临时视图供 SQL 使用  

```python
from pyspark.sql.types import StructType, StructField, IntegerType

schema = (
    StructType()
    .add("id", IntegerType(), nullable=False)
    # .add("name", StringType(), True)
)
```

![1751118806089](../img/1751118806089.png)

![1751118874003](../img/1751118874003.png)

### DSL 常用 API

```python
df.select("col_name").show()
df.filter("score < 90")
df.filter(df["score"] < 90)
df.where(df["score"] < 90)
df.groupBy("subject").count().show()

from pyspark.sql import functions as F

df.dropDuplicates(["id"])
df.dropna()
df.fillna({"score": 0})
```

![1751119111794](../img/1751119111794.png)

![1751119401322](../img/1751119401322.png)

![1751119692050](../img/1751119692050.png)

![1751119744600](../img/1751119744600.png)

![1751119794328](../img/1751119794328.png)

![1751120368114](../img/1751120368114.png)

窗口函数：`rank()`、`dense_rank()`、`row_number()` over (...)

![1751120616737](../img/1751120616737.png)

![1751120713285](../img/1751120713285.png)

![1751120744363](../img/1751120744363.png)

![1751120782745](../img/1751120782745.png)

![1751120872090](../img/1751120872090.png)

![1751120961264](../img/1751120961264.png)

![1751121309224](../img/1751121309224.png)

Catalyst：**AST（未解析逻辑计划）→ 逻辑计划（谓词下推、列裁剪等）→ 物理计划**

![1751121556471](../img/1751121556471.png)

![1751121576637](../img/1751121576637.png)

![1751162496734](../img/1751162496734.png)

![1751162809849](../img/1751162809849.png)

Hive Metastore 端口排查（示例）：`netstat -anp | grep 9083`  
Shell：`/bin/pyspark`、`/bin/spark-sql`

![1751163634395](../img/1751163634395.png)

## Spark 新特性（AQE）

![1751163707750](../img/1751163707750.png)

![1751163910598](../img/1751163910598.png)

![1751164205074](../img/1751164205074.png)

![1751164302798](../img/1751164302798.png)

![1751164364065](../img/1751164364065.png)

**AQE（Adaptive Query Execution）**

- 动态合并 Shuffle 分区  
- 动态调整 Join 策略  
- 动态优化倾斜 Join（skew join）  

![1751164609986](../img/1751164609986.png)

![1751164675729](../img/1751164675729.png)

![1751164808835](../img/1751164808835.png)

![1751164897180](../img/1751164897180.png)

![1751164934712](../img/1751164934712.png)

![1751165195854](../img/1751165195854.png)

![1751165251826](../img/1751165251826.png)

![1751165391657](../img/1751165391657.png)

![1751165472186](../img/1751165472186.png)

![1751165515789](../img/1751165515789.png)

![1751165576154](../img/1751165576154.png)

![1751165613866](../img/1751165613866.png)

![1751165653315](../img/1751165653315.png)

![1751165685380](../img/1751165685380.png)

![1751165744793](../img/1751165744793.png)

## Spark Core（补充）

Spark 3.5.x 发行包：[archive.apache.org/dist/spark/spark-3.5.6](https://archive.apache.org/dist/spark/spark-3.5.6/)


分布式计算需要:
• 分区控制
• Shuffle控制
• 数据存储\序列化\发送
• 数据计算API
• 等一系列功能
这些功能, 不能简单的通过Python内置的本地集合对象(如 List\ 字典等)去完成.
我们在分布式框架中, 需要有一个统一的数据抽象对象, 来实现上述分布式计算所需功能.
这个抽象对象, 就是RDD

RDD定义
RDD（Resilient Distributed Dataset）叫做弹性分布式数据集，是Spark中最基本的数据抽象，代表一个不可变、可
分区、里面的元素可并行计算的集合。
Dataset：一个数据集合，用于存放数据的。
Distributed：RDD中的数据是分布式存储的，可用于分布式计算。
Resilient：RDD中的数据可以存储在内存中或者磁盘中。

![1751290273773](../img/1751290273773.png)

RDD 5大特性：

1. RDD 是有分区的
2. RDD 的方法会作用在所有的分区上
3. RDD 之间是有血缘关系
4. key-Value 型的RDD 可以有分区器
5. RDD 的分区规划，会尽量靠近数据所在服务器

![1751290564124](../img/1751290564124.png)

RDD 算子：

- Transformation 算子

- Action 算子

RDD 的数据是过程数据：

RDD 之间进行相互迭代计算，当执行开启后，新的RDD的生成，代表老的RDD 消失，这个特性可以最大化利用资源，老旧的RDD 就从内存中清理，给后续的计算腾出空间

RDD

- 广播变量
- 累加器

作业层级：`Application → Job → DAG → Stage（Shuffle 切分）→ Task`

![1751293706609](../img/1751293706609.png)




## 参考链接

- [黄汉宇 — Spark 笔记 1](https://www.cnblogs.com/huanghanyu/p/12988879.html)
- [知乎 — Spark 相关](https://zhuanlan.zhihu.com/p/636284371)
- [黄汉宇 — Spark 笔记 2](https://www.cnblogs.com/huanghanyu/p/12989067.html)
- [B 站课程（第 41 集）](https://www.bilibili.com/video/BV1Jq4y1z7VP?p=41)
