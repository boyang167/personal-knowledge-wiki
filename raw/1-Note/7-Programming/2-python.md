# Python 笔记

个人 Python / NumPy / Pandas 学习与实践笔记（含并发、设计模式等）。

## 目录

- [Python 语言](#python-语言) — 基础语法、OOP、IO、并发、collections、设计模式
- [NumPy](#numpy)
- [Pandas](#pandas) — 清洗、生成、`describe` / `apply`、索引与类型

---

## Python 语言

### 基础语法

#### 函数

1： 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

2： 如果没有`return`语句，函数执行完毕后也会返回结果，只是结果为`None`

3：函数可以同时返回多个值，但其实就是一个tuple:

4：定义默认参数要牢记一点：默认参数必须指向不变对象！

~~~
def add_end(L=[]): # 默认参数
    L.append('END')
    return L
add_end()
add_end()
['END', 'END']
函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
~~~

5：可变参数

允许在list或tuple前面加一个`*`号，把list或tuple的元素变成可变参数传进去

6： 关键字参数

关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

7： 命名关键字参数

关键字参数`**kw`不同，命名关键字参数需要一个特殊分隔符`*`，`*`后面的参数被视为命名关键字参数。

~~~
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
~~~

8：参数组合

~~~
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
~~~

9： 高阶函数  闭包 

~~~python
既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
“MapReduce: Simplified Data Processing on Large Clusters”

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易

返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。 

~~~

10： Map ,reduce

~~~python
map : 函数接收两个参数，一个是函数，一个是Iterable
将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

reduce
把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
	return x + y
reduce(add, [1, 3, 5, 7, 9])
# 把序列[1, 3, 5, 7, 9]变换成整数13579，
def fn(x, y):
    return x * 10 + y
reduce(fn, [1, 3, 5, 7, 9]) 


from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
~~~

11：`filter()`函数用于过滤序列 筛选”函数

~~~python
filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def not_empty(s):
    return s and s.strip()
list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']

~~~

12： sorted

~~~python
sorted([36, 5, -12, 9, -21], key=abs)

~~~

13: lambda 

~~~
们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
~~~

14 ： 偏函数

~~~
int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
import functools
就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
int2 = functools.partial(int, base=2)
当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
~~~





#### 迭代器与生成器

~~~python
如何判断一个对象是可迭代对象呢？
方法是通过collections.abc模块的Iterable类型判断：
from collections.abc import Iterable
#enumerate
for i, value in enumerate(['A', 'B', 'C'])
	pass

for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码
for x, y in [(1, 1), (2, 4), (3, 9)]:
     print(x, y)

集合数据类型，如list、tuple、dict、set、str等
一类是generator，包括生成器和带yield的generator function。
for循环的对象统称为可迭代对象：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象：

isinstance([], Iterable)

凡是可作用于for循环的对象都是Iterable类型
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
~~~

#### 列表生成式：

~~~python
[x for x in range(1, 11) if x % 2 == 0 else 0]
isinstance(variable_name ,str)

~~~

生成器：

~~~python
generator
生成器都是Iterator对象
Iterator对象表示的是一个数据流，数据流看做是一个有序序列，但我们却不能提前知道序列的长度

g = (x * x for x in range(10))

yield关键字
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
1: 用for 循环不会保错
2： next 最后会报错
while True:
     try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
         print('Generator return value:', e.value)
        break
~~~

#### 装饰器

~~~python
由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
f = sum()
f(1,2,3)
函数对象有一个__name__属性，可以拿到函数的名字

在代码运行期间动态增加功能的方式，称之为“装饰器” Decorator
decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)  # 日志功能
        return func(*args, **kw)
    return wrapper

Python的@语法，把decorator置于函数的定义处：


~~~

### 面向对象（class）

~~~python
class后面紧接着是类名，即Student，类名通常是大写开头的单词

class Student(object):   # 所有类最终都会继承的类 object
    def __init__(self ,name ,score) :
        self.__name = name
        self.score = score
        pass 
    def get_name(self):
        return self.__name
    def set_score(self, score):
        self.__score = score
    pass
#访问限制
1：如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
2：如果外部代码要获取name和score怎么办？
可以给Student类增加get_name和get_score这样的方法：
 def get_name(self):
        return self.__name
    
3：#双下划线开头的实例变量是不是一定不能从外部访问呢？
 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
 所以，仍然可以通过_Student__name来访问__name变量：  
bart = Student('Bart Simpson', 59)
bart.get_name() 'Bart Simpson' 
bart.__name = 'New Name' # 设置__name变量！
bart.__name
表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：

4: 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到
del s.name # 如果删除实例的name属性
在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。


~~~

继承

~~~
继承有什么好处？
1：最大的好处是子类获得了父类的全部功能
2：子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。

3：在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：

~~~

判断类型

~~~
动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
isinstance
type
dir

type()函数既可以返回一个对象的类型，又可以创建出新的类型，
要创建一个class对象，type()函数依次传入3个参数：

class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

~~~

如果我们想要限制实例的属性怎么办

~~~python
__slots__
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

@property   装饰器就是负责把一个方法变成属性调用的：
属性的方法名不要和实例变量重名

__str__
__repr__
__iter__ 迭代对象
__getitem__
__call__  一个对象实例可以有自己的属性和方法， 对实例进行直接调用就好比对一个函数进行调用一样

class Student(object):
    def __init__(self, name):
        self.name = name
	def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('Michael')s() 
# self参数不要传入
通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。


metaclass

~~~

##### 枚举

~~~python
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

from enum import Enum, unique #  @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

~~~

### 异常处理

~~~python
try:
    pass
except  Exception as e:
    pass 
finally:
    pass 
用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕


Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：

try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。  

凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
logging.basicConfig(level=logging.INFO)


~~~

### 日志

~~~
import logging

logging.exception(e)
logging.info('n = %d' % n)
~~~



### 读写 IO

~~~python
1: 读取文件
open
read
2： 内存文件
StringIO
BytesIO
StringIO顾名思义就是在内存中读写str。
from io import StringIO
f = StringIO()
f.write('hello')
f.getvalue()

import os
os.name # 操作系统类型
os.uname()
os.environ  环境变量
os.environ.get('PATH')
3：操作文件和目录
#查看当前目录的绝对路径:
os.path.abspath('.')
os.path.join()
os.mkdir()
os.rmdir()
os.path.split('/Users/michael/testdir/file.txt') #要拆分路径时，也不要直接去拆字符串
os.path.splitext() #可以直接让你得到文件扩展名，很多时候非常方便：
os.rename('test.txt', 'test.py')
os.remove('test.py')
如何获取当前模块的文件名
print(__file__)
import sys
print(sys.argv)
print(sys.executable)
shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充
[x for x in os.listdir('.') if os.path.isdir(x)]
要列出所有的.py文件，也只需一行代码：
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
~~~



### 序列化（pickle / JSON）

~~~
把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
import pickle
1:pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)

2: json

JSON类型	Python类型
{}	dict
[]	list
"string"	str
1234.56	int或float
true/false	True/False
null	None
import json
son.dumps(d)
 json.loads(json_str)
~~~



### 线程

~~~python
多任务：
并发： cpu 轮循
并行  同时执行 多核
进程： process 是分配资源的最小单位，它是操作系统进行资源分配和调度运行的基本单位
线程： 是计算机可以被调度cpu最小的单位
一个进程中的多个线程可以共享该进程的资源
多进程 完成多任务
GIL Global interpreter lock cpython
GIL 锁是cpython 解释器特有的一个全局解释器锁， 控制一个进程中同一时刻只有一个线程可以被cpu调度
列表，字典 常见对象的是线程安全的 
计算密集型： 多进程
IO密集型 ： 多线程 文件

#进程的创建 
import multiprocessing 
import threading
obj = multiprocessing.Process(target )
obj.start()

# threading  
start()  #准备就绪 等待CPU调度 ，具体时间由CPU决定
join()  # 等待当前线程执行完毕后再向下继续执行 
.setDaemon(boolean) , 守护线程 ，
queue() 
# 数据安全加锁  
2种  RLock 递归锁  Lock 不能嵌套 锁多次 容易死锁
死锁情况： 各自拿着锁，请求对方锁 。 

look = threading.RLock()
lock.acquire()  # 加锁
lock.release()  # 释放锁 

# 线程池
from concurrent.feature import ThreadPoolExcutor

pool.submit()
pool.shutdown(True) # 等待线程池线程执行完，才继续执行

# 在线程池提交一个任务，线程池中如果有空闲线程，则分配一个去执行，执行完后再将线程交换给线程池，如果没有空闲线程，则等待 
res = pool.submit(task_name , paramaters )# 下载
res.add_done_callback(task_2)  # 保存 
python 线程安全 

~~~

### 多进程

~~~python
进程之间是相互隔离的 多核优势
fork 创建 放在main  forl spawn forkserver
import multipricessing
fork 模型 子进程会拷贝主进程的所以值 资源   任意位置开始 
文件 fork 都可以  拷贝的锁是主进程被上锁的状态

forkserver ，spawn 模型 参数会传递   但是两份数据 会各自维护自己的数据  main 位置开始


# 常见的方法
p.start()  # 准备就绪，等待cpu 的调度  ， 主线程执行任务
p.join() # 等待
p.daemon() # 守护进程 必须放在start 之前 

#自定义进程类 ，直接将线程要做的事情，写到run 方法中

multiprocessing.cpu_count() # 获取cpu的个数
class MyProcess(multiprocessing.Process):
    def run(self):
        pass
# 进程数据共享  默认是相互独立的
1:Value , Array 使用参数传递 
arr = Arrat('i',[1,2,3]) # i  int 
2: 交换
    Manager
    d = Manager.dict()
3: Queues 队列 
    que = multiprocess.Queue()
    que.put()
    que.get()
4： Pipes 
	parent , child = multiprocessing.Pipe()
    
进程A  redis
进程B  redis   

# 进程锁 
多个进程抢占的去做某些操作 ， 为了数据出问题，可以通过进程锁来避免

进程锁可以传 
lock = multiprocessing.Process(target= tesk , args =(lock,))

# 进程池
from concurrent.futures import ProcessPoolExecutor

pool.shutdown(True) # 阻塞 直到所有进程执行完 ， 才继续执行

fur = pool.submit(task ,i)
fur.add_done_callback(task) #调用主进程处理 

current_process().pid()




~~~

~~~python
# eg1 :

def task(file_name , count_dict):
    count_dict[file_name] = {'total': v,'ip':v2}
    
def run():
    pool = ProcessPoolExcutor(4)
    with Manager() as mg :
        count_dict = mg.dict() # 进程数据共享 
        for fine_name  in os.listdir('path'):
        	pool.submit(task , file_name,count_dict)
        pool.shutdown(True)
        
# eg2 : 
def task(file_name ):
    return {'total': v,'ip':v2}

def outer(info , file_name):
    def done(res , *args ,**kwargs):
        infp[file_name] = res.result()
    return done 

def run():
    info ={}
    pool = ProcessPoolExcutor(4)
    for fine_name  in os.listdir('path'):
        fur = pool.submit(task , file_name)
        fur.add_done_callback(outer(info,file_name)) #  回调函数 只能传函数， 如果有参数使用闭包
     pool.shutdown(True)
~~~

### 协程

协程称为微线程， IO 请求 ， 多个IO 同时 ，等待时间可以利用

是一种用户态内的上下文切换技术， 



~~~python
1: 闭包

2： 单例模式 
import threading 
class Singleton :
    instance = None
    lock = threading.Rlock()
    def __new__(cls, *args ,**kwargs):
        if cls.instance :
            return cls.instance
        with cls.lock:
            if cls.instance :
            	return cls.instance
            cls.instance = object.__new__(cls)
        return cls.isntance 
  



~~~



### collections 与 itertools

~~~python
1:namedtuple是一个函数，它用来创建一个自定义的tuple对象， 一个点的二维坐标就可以表示成：

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

2:deque
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
3:defaultdict
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
 from collections import defaultdict
 dd = defaultdict(lambda: 'N/A')
4: OrderedDict 保持Key的顺序
  OrderedDict的Key会按照插入的顺序排列，不是Key本身排序

5:ChainMap
6: Counter
    
import itertools
无限”迭代器
natuals = itertools.count(1)
count()会创建一个无限的迭代器
cycle()会把传入的一个序列无限重复下
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
ns = itertools.takewhile(lambda x: x <= 10, natuals)
chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
groupby()把迭代器中相邻的重复元素挑出来放在一起：

并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。

实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法：
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    
    def query(self):
        print('Query info about %s...' % self.name)
        
编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：
from contextlib import contextmanager
@contextmanager
~~~

### 文件读写与 `*` 解包速查

`shift + tab`（Notebook 缩进）

```text
open
 a+ 定位到文件末尾 
f.seek(0) # 移动到开始位置 
f.read()
f.readline() # 读取表头


f.write() #  写在内存   
f.flush() # 写在磁盘 
*[1,3,4]
列表前面加星号作用是将列表解开成 len(list) 个独立的参数，传入函数
字典前面加1个星号，是将字典key解开成独立的元素作为形参。
字典前面加2个星号，是将字典value解开成独立的元素作为形参。


读取json 
next(csv.reader(f))
map(lammda x : x ,迭代对象 ) #迭代对象[]  ,{}等
res = [{key:v}m]
list(map(lambda v: {"genre": v[0], "count": v[1]}, res))
```

### 列表与函数式编程速查

```python
.clear()
append() 
extend()
insert(index, values)
remove(values)
pop()
count(x)
B = reverse(A)
A.index(value) # 返回第一个为x 的值
list(enumerate(list))
sort()
sorrted
lambda x , y : x+y 
map(func, *iterabale)

filter()
def is_None(arr):
    return arr and len(arr.strip())>0
arr =[' ' ,'12','hello']
print([*filter(is_None,arr)])

reduce()
from functools import reduce
a = [1,2,3,4,5]

列表推导式
print(reduce(lambda x, y:x+y, a))
[i for i in  list if i>3]

dic = {'key1':1 ,'key2':2,'key3':3}
keys = [key for key ,value in dic.items()]
dic2 ={value:key for key ,value in dic.items()}
print(keys)

闭包： 一个返回值是函数的函数
def make_filter(key_words):
	def the_filer(file_name):
		file = open(file_name)
		lines = file.readlines()
		file.close()
		filter_doc = [i for i in lines if keep in i]
		return filter_doc
	return the_filter
filter1 = make_filter('word')
filter_res = filter1('data.csv')
```

> 装饰器原理与 `@` 语法见上文 [装饰器](#装饰器)。

### os / 环境变量速查

```python
os.path.dirname(__file__) #返回当前路径
oenviron
os.system("unzip dev_data.json.zip") # 执行命令
f.readline() 读取一行  包含\n
f.readlines() 读取所有
2. 查看所有对象
   print(dir(os))
   print(dir(os.path))
   import os
""" 
    os.name                     当前操作系统 Windows: nt, Linux: posix
    os.sep                      分隔符
    os.getcwd()                 当前工作目录
    os.chdir(path)              切换当前工作目录
    os.listdir(path)            返回 文件 和 目录 列表
    os.walk(path)               返回 文件 和 目录 列表(含 子目录 = 递归)
    os.rename(src, dst)         重命名文件，从 src 到 dst
    os.renames(old, new)        重命名文件（含 子目录 = 递归）
    os.remove(path)             删除文件
    os.path.abspath(path)       返回绝对路径
    os.path.basename(path)      返回文件名
    os.path.dirname(path)       返回路径名
    os.path.exists(path)        路径存在，返回 True，反之，返回 False
    os.path.lexists(path)       路径存在，返回 True，路径损坏也返回True，不存在，返回 False
    os.path.getmtime(filename)  返回最后修改时间（浮点型秒数）
    os.path.getatime(filename)  返回上次访问时间（浮点型秒数）
    os.path.getctime(filename)  返回元数据更改时间（浮点型秒数）
    os.path.getsize(filename)   返回文件大小（字节）
    os.path.isabs(path)         判断是否为 绝对路径
    os.path.isfile(path)        判断是否为 文件
    os.path.isdir(path)         判断是否为 目录
    os.path.islink(path)        判断是否为 链接
    os.path.join(path, *paths)  把目录和文件名合成一个路径
"""
print(f'当前操作系统: {os.name}')
print(f'分隔符: {os.sep}')
path = os.getcwd()
print(f'当前工作目录: {path}')
last_modify_time = os.path.getmtime(path)
print(f'最后修改时间: {last_modify_time}')
print(f'最后修改时间: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(last_modify_time))}')
print(os.path.join(path, '123'))

import os
os.environ['JAVA_HOME'] = r'C:\servies\Java\jdk8'  
os.environ['SPARK_HOME'] = r'D:\software\spark-2.2.0-bin-hadoop2.7'
os.environ['PYTHONPATH'] = r'D:\software\spark-2.2.0-bin-hadoop2.7\python'

```

### 设计模式

~~~
封装  继承 多态  接口 

接口：  继承类要实现接口方法
from abc import ABCMeta , abstractmethod
@abstractmethod
继承抽象类， 必须实现抽取方法 

solid 原则
开放封闭式原则：
里氏替换原则：
依赖倒置原则：
接口隔离原则
单一职责原则
设计模型分类：
创建型模式5种： 
工厂模型 ，抽象工厂， 创建者模式 ，原型模式， 单例模式
结构模式7种：
适配器模式，桥模式， 组合模式， 装饰模式， 外观模式， 享元模式， 代理模式
行为型模式： 11 种
解释器模式，责任链模式，命令模式， 迭代器模式， 中介模式，备忘录模式，观察者模式，状态模式，策略模式，访问者模式， 模板方法模式，

1简单工厂模式
不能直接向客服端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品的实例 
角色：
工厂角色  creator
抽象产品角色 product
具体产品角色 Concreate Prodext

2工厂方法模式
抽象工厂角色 Creator
具体工厂角色  Concrete creator
抽象产品角色 product
具体产品角色 Concreate Prodext
优点： 
1：每个具体产品都对应一个具体工厂类， 不需要修改工厂类代码
2： 隐藏了对象创建的实现细节
缺点： 每增加一个具体产品类，就必须增加一个相应的具体工厂类

3: 抽象工厂模式
内容： 定义一个工类接口， 让工厂子类来创建一系列相关或者相互依赖的对象
相比工厂方法模式，抽象工厂模式中的每个具体的工厂都生产一套产品
抽象工厂角色 Creator
具体工厂角色  Concrete creator
抽象产品角色 product
具体产品角色 Concreate Prodext
客服端 
每个工厂创建一套完整的产品系列 ，使得易于交换产品系列
有利于产品的一致性
缺点： 难以支持新种类 抽象产品 

4： 建造者模式 
内容：  将一个复杂的对象构建与它的表示分离 ， 使得同样的构建过程可以创建不同的表示
角色： 
抽象创建者  builder
具体的建造者 concrete builder
指挥者 Direcotr
产品 Product
优点： 隐藏了一个产品的内部结构和装配过程
将构造代码与表示代码分开
可以对构造过程进行更精细的控制


5：单例模式 Single
1：类创建对象 ，在内存中只有唯一个实例
2： 每一次实例化生成对象， 内存地址是相同的

优点： 
对唯一实例受控访问
单例相当于全局变量， 但防止了命名空间被污染


__new__ :
是object 基类提供的内置静态方法
在内存中为对象分配空间
返回对象的引用
python 解释器在获得对象引用后， 将引用作为第一个出参传递给__init__方法


~~~

简单工厂模式

~~~python
from abc import ABCMeta ,abstractmethod
class Payment(metaclass = ABCMeta):   #抽象产品角色 product
    @abstractmethod
    def pay(self,money):
        pass
class AliPay(Payment):  #具体产品角色 Concreate Prodext
    def pay(self, money):
        print('alipay')
class WechatPay(Payment): #具体产品角色 Concreate Prodext
    def pay(self, money):
        print('wechatpay')    
class PaymentFactory:  # 简单工厂模式   工厂角色  creator
    def creat_payment(self,method):
        if method == 'alipay':
            return Alipau()
        elif method =='wechat':
            return WechatPay()
        else :
            raise TypeError('')
     
~~~

工厂方法模式

~~~~python
from abc import ABCMeta ,abstractmethod
class Payment(metaclass = ABCMeta):   #抽象产品角色 product
    @abstractmethod
    def pay(self,money):
        pass
class AliPay(Payment):  #具体产品角色 Concreate Prodext
    def pay(self, money):
        print('alipay')
class WechatPay(Payment): #具体产品角色 Concreate Prodext
    def pay(self, money):
        print('wechatpay')    

class PaymentFactory(metaclass=ABCMeta):  #  抽象工厂角色 Creator
    @abstractmethod
    def creat_payment(self,method):
        pass
class AlipayFactory(PaymentFactory): #具体工厂角色  Concrete creator
    def creat_payment(self):
        return AliPay()
class WechatPayFactory(PaymentFactory):
    def creat_payment(self):
        return WechatPay()
~~~~

3: 抽象工厂模式

~~~python
#  生产一部手机 ，  手机壳， CPU， OS 进制组装 ，其中每个类对象都有不同的种类
# 相比工厂方法模式， 抽象工厂模式中每个具体的工厂都生产一套产品
from abc import ABCMeta ,abstractmethod
# 抽象产品
class CPU(metaclass = ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass
class OS(metaclass = ABCMeta):
    @abstractmethod
    def show_os(self):
        pass
# 抽象工厂
class PhoneFactory(metaclass = ABCMeta):
    @abstractmethod
    def make_cpu(self):
        pass
    @abstractmethod
    def make_os(self):
        pass
# 具体产品
class SnapDragonCpu(CPU):
    def show(self):
        print('snapDragon cpu')
class AppleCpu(CPU):
    def show(self):
        print('AppleCpu cpu')
class Anroid(OS):
    def show_os(self):
        print('android os')
class IOS(OS):
    def show_os(self):
        print('IOS os') 
# 具体工厂   多个工厂 
class MiFacotry(PhoneFactory):  
    def make_cpu(self):
        return SnapDragonCpu()
    def make_os(self):
        return Anroid()
class HuaweiFactory(PhoneFactory):
   	def make_cpu(self):
        return SnapDragonCpu()
    def make_os(self):
        return Anroid() 
# 客服端 
class Phone:
    def __init__(self, cpu,os):
        self.cpu = cpu
        self.os = os
  

~~~

4： 建造者模式 

~~~~python
from abc ABCMEta ,abstractmethod
class Player:
    def __init__(self, face = None , body=None ,arm =None ,leg =NOne):
        self.face =face 
        self.body = body
        self.arm = arm
        self.leg = leg
     def __str__(self):
        return "%s ,%s,%s,%s,"%(self.face,...)
class PlayBuilder(metaclass = ABcMeta):
    @abstractmethod
    def build_face(self):
        pass
    @abstractmethod
    def build_body(self):
        pass
class SexyGirlBuilder(PlayBuilder):
    def __init__(self):
        self.player =Player()
    def build_face(self):
        self.player.face = 'beautiful face'
    def build_body(self):
        self.player.body = '苗条'
        
class MonsterPlayer(PlayBuilder):
    def __init__(self):
        self.player =Player()
    def build_face(self):
        self.player.face = 'monster face'
    def build_body(self):
        self.player.body = '苗条'  
class PlayerDirector:  # 控制组装顺序
    def build_player(self,builder):
        builder.build_body()
        builder.build_face()
        return builder.player()
#client
builder = SexyGirlBuilder()
director = PlayerDirector()
p = director.build_player(builder)

~~~~

5 单例模式

~~~python

# 看地址  id()
class Singleton:
    def __new__(cls ,*arg ,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._isntance = super(Singleton,cls).__new__(cls) # 调用父类创建
         return cls._instance
class Myclass(Singleton):
    def __init__(self,a):
        self.a = a 
a = Myclass(10)
b = Myclass(20)
        
~~~







---

## NumPy

增加维度：`np.newaxis`  
降维：`np.ravel()`

常用 API 速查：

```python
np.transpose()
np.where(condition, value1, value2)
# argmax, argmin, cumsum
np.save()   # .npy
np.load()
np.savez('path', variable=x1, variable2=x2, ...)
np.savetxt('1.txt', arr, delimiter=',')
# dot, trace, det, eig
```

---

## Pandas

数据清洗与特征处理示例：

data.drop(["Cabin","Name","Ticket"],inplace=True,axis=1)

data["Age"] = data["Age"].fillna(data["Age"].mean())
data = data.dropna()

data["Embarked"] = data["Embarked"].apply(lambda x: labels.index(x))

drop_duplicates(inplace = True) # 删除以后，要恢复索引

df.melt()

```python
# 去除重复值
df.duplicated()
df.drop_duplicates()
# 查看各字段缺失率
df.info()

# 缺失值按均值填充
for col in list(df.columns[df.isnull().sum() > 0]):
    mean_val = df[col].mean()
    df[col].fillna(mean_val, inplace=True)
    
  # 删除不分析的列
columns =["col_name"]
df.drop(columns,axis=1,inplace=True)


```

### 数据生成与 describe / cut / apply





~~~python
index = pd.date_range("1/1/2000", periods=8)  # 时间序列
series = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])

1: describe()方法来对表格中的数据做一个概括性的统计分析，
df.describe(percentiles=[0.05, 0.25, 0.75, 0.95]) # 分位数
要是表格中既包含了离散型数据，也包含了连续型的数据，默认的话，
describe()是会针对连续型数据进行统计分析
df2.describe(include=["object"]) 指定让其强制统计分析离散型数据或者连续型数据
include = ['object','number','all']
2: idxmin()和idxmax()方法是用来查找表格当中最大/最小值的位置，返回的是值的索引

3: value_counts()方法主要用于数据表的计数以及排序 ,同时里面也还可以利用参数normalize=True，来计算不同值的计数占比
df['col_name'].value_counts(ascending=True,normalize=True)
4: 数据分组
cut()方法以及qcut()方法来对表格中的连续型数据分组
ages = np.array([2,3,10,40,36,45,58,62,85,89,95,18,20,25,35,32])
pd.cut(ages, 5)  pd.cut(ages, 5, labels=[u"婴儿",u"少年",u"青年",u"中年",u"老年"])
pd.qcut(ages, [0,0.5,1], labels=['小朋友','大孩子'])

5:引用函数
pipe()
首先我们来看pipe()这个方法，我们可以将自己定义好的函数，以链路的形式一个接着一个传给我们要处理的数据集上
apply()和applymap()
agg()和transform()

def extract_city_name(df):
    df["state_name"] = df["state_and_code"].str.split(",").str.get(0)
    return df

def add_country_name(df, country_name=None):
    df["state_and_country"] = df["state_name"] + country_name
    return df
df_p = pd.DataFrame({"city_and_code": ["Arizona, AZ"]})
df_p = pd.DataFrame({"state_and_code": ["Arizona, AZ"]})
df_p.pipe(extract_city_name).pipe(add_country_name, country_name="_USA")

apply()方法可以对表格中的数据按照行或者是列方向进行处理，
apply()方法和applymap()方法

df.apply(np.mean,axis=1)
df.apply(lambda x: x.max() - x.min(),axis=1)
def normalize(x):
    return (x - x.mean()) / x.std()
df.apply(normalize)

apply()方法作用于数据集当中的每个行或者是列，而applymap()方法则是对数据集当中的所有元素都进行处理
def add_A(x):
    return "A" + str(x)
df = pd.DataFrame({'key1' : ['a', 'c', 'b', 'b', 'd'],
                   'key2' : ['one', 'two', 'three', 'two', 'one'],
                   'data1' : np.arange(1, 6),
                   'data2' : np.arange(10,15)})
df.applymap(add_A).applymap(lambda x: x.split("A")[1])


agg()方法和transform()方法
agg()方法本意上是聚合函数，我们可以将用于统计分析的一系列方法都放置其中，并且放置多个
df.agg(np.sum)
当然，当中的np.sum部分也可以用字符串来表示，例如
df.agg("sum")
df.agg(["sum", "mean", "median"])
df.agg(["sum", lambda x: x.mean()])
与此同时，我们在agg()方法中添加字典，实现不同的列使用不同的函数方法
df.agg({"A": "sum", "B": "mean"})
df.agg({"A": ["sum", "min"], "B": "mean"})
~~~

### 索引重命名、排序与类型

~~~
1: 重命名
df1 = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"],
                   index = ["a", "b", "c", "d", "e"])
                   
df1.rename(columns={"A": "one", "B": "two", "C": "three"},
                 index={"a": "apple", "b": "banana", "c": "cat"})
                 
df1.rename({"A": "one", "B": "two", "C": "three"}, axis = "columns")
df1.rename({"a": "apple", "b": "banana", "c": "cat"}, axis = "index")对行的重命名则可以这么来做
2： 排序
df1.sort_values(by = "col_name1")
df1.sort_values(by = ["col_name1","col_name2",...],ascending=False)
3: 数据转换
最后涉及到的是数据类型的转换，在这之前，我们先得知道如何来查看数据的类型
通过dtypes属性来查看数据的类型
而通过astype()方法来实现数据类型的转换
df2["B"].astype("int64")


们也可以根据相对应的数据类型来进行筛选，运用pandas当中的
select_dtypes方法，我们先来创建一个数据集包含了各种数据类型的
df = pd.DataFrame(
    {
        "string_1": list("abcde"),
        "int64_1": list(range(1, 6)),
        "uint8_1": np.arange(3, 8).astype("u1"),
        "float64_1": np.arange(4.0, 9.0),
        "bool1": [True, False, True, True, False],
        "bool2": [False, True, False, False, True],
        "dates_1": pd.date_range("now", periods=5),
        "category_1": pd.Series(list("ABCDE")).astype("category"),
    }
)
df.dtypes
df.select_dtypes(include=[bool])
df.select_dtypes(include=['int64'])
~~~



