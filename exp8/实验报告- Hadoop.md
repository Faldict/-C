# 实验报告: Hadoop

###### 姓名：王嘉璐
###### 班级：F1503023

## 在Docker上运行Hadoop

### 为什么要用Docker

在做本实验的过程中，首先要按照冗长复杂的安装说明安装Hadoop。这一过程不仅会耗费同学们大量的时间，而且有的同学一直卡在某一步上，无法解决；也有很多同学即使装好了Hadoop也稍有不慎就把虚拟机搞崩。**最后，很多同学都是直接拷贝的其他已经装好Hadoop的同学的虚拟机来完成实验。**况且我认为安装Hadoop的过程与本实验并无关联，毫无意义而且浪费时间。所以，我想到**在一个已经安装好Hadoop的容器上进行实验。**而Docker是世界上最主要的软件容器化架构，而且在Docker Hub上提供了很多软件镜像，这就是我选择使用Docker的原因。

### 在Docker上安装Hadoop

在使用Docker之前首先要安装Docker,安装方法可以参考官网上的<a href="https://www.docker.com/products/docker#/mac">说明</a>，下载相应系统的Docker文件来安装。  

安装好Docker之后，在Docker Hub上查找Hadoop的镜像。在这里我使用的是Hadoop的<a href="https://hub.docker.com/r/sequenceiq/hadoop-docker/">官方镜像</a>。  

然后打开终端使用如下命令将此镜像拉下来。

```
docker pull sequenceiq/hadoop-docker:2.7.0
```
最后的`2.7.0`是Hadoop的版本号，在安装说明中使用的是2.2.0版本的，太过于陈旧甚至不支持64位系统，所以我这里选择了最新的2.7.0版本。实际上你可以根据自己需求自行选择。  

把镜像拉下来后就可以直接运行了：

```
docker run -it sequenceiq/hadoop-docker:2.7.0 /etc/bootstrap.sh -bash
```

这样进入的是一个SELinux系统的Bash，注意在这个系统里Hadoop并不是全局命令。

输入`jps`可以看到六个进程都已经在运行了，然后切换到Hadoop的文件目录：

```
cd $HADOOP_PREFIX
```

在这个容器里`$HADOOP_PREFIX=/usr/local/hadoop`。  

接下来可以运行一些程序进行测试：

```
# run the mapreduce
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.0.jar grep input output 'dfs[a-z.]+'

# check the output
bin/hdfs dfs -cat output/*
```
> Note: 由于Hadoop不是全局命令，在实验指导上的所有hadoop命令前面都要加上`bin/`才可以在这个容器上正确运行。

如果要把文件移动到docker容器内，可以使用`docker cp`命令。需要注意的是，在使用这个命令之前通过`docker ps`找到docker容器的id。

## Hadoop的例子

### 使用MapReduce计算文本的词数

在Map中，把文本的每一行都分割成一个一个的单词并计数为1，然后排序后在Reduce里，把相同单词的计数合并起来，便得到所有单词的频数。

### 蒙特卡洛方法计算圆周率

首先，在平面直角坐标系中，假设存在一个[-1,1]x[-1,1]的正方形，在此正方形内有一半径为1的圆。在Map阶段向正方形内随机掷一点，判断此点是否在圆上。在Reduce阶段求出所有在圆上的点的数目，再除以总共实验的数目，就可以得到圆和正方形面积的比值。这个比值再乘以4就是圆周率。实际过程中可以通过大量重复实验的次数来提高计算得到的圆周率的精度。

下表是在不同参数下用Hadoop mapreduce example PI计算得到的圆周率值和运行时间：  

| Number of Maps | Number of samples | Time | PI |
| -------------- | ----------------- | ---- | -- |
| 2 | 10 | 15.015 | 3.8 |
| 5 | 10 | 16.897 | 3.28 |
| 10 | 10 | 18.942 | 3.2 |
| 2 | 100 | 14.895 | 3.12 |
| 10 | 100 | 17.908 | 3.148 |
| 100 | 1000 | 106.414 | 3.1412 |
| 10 | 10000 | 18.958 | 3.1412 |
| 5 | 200000 | 15.892 | 3.141552 |
| 10 | 100000 | 18.911 | 3.141552 |
| 10 | 400000 | 18.929 | 3.141604 |
| 10 | 4000000 | 19.925 | 3.1415981 |

可以看到影响运算时间的主要参数是`Number of Maps`，而`Number of samples`的影响不是很大。

## PageRank

以下代码定义了一个mapreduce操作。

``` Python
# map_reduce.py
# Defines a single function, map_reduce, which takes an input
# dictionary i and applies the user-defined function mapper to each
# (input_key,input_value) pair, producing a list of intermediate
# keys and intermediate values.  Repeated intermediate keys then
# have their values grouped into a list, and the user-defined
# function reducer is applied to the intermediate key and list of
# intermediate values.  The results are returned as a list.

import itertools

def map_reduce(i,mapper,reducer):
  intermediate = []
  for (key,value) in i.items():
    intermediate.extend(mapper(key,value))
  groups = {}
  for key, group in itertools.groupby(sorted(intermediate),
                                      lambda x: x[0]):
    groups[key] = list([y for x, y in group])
  return [reducer(intermediate_key,groups[intermediate_key])
          for intermediate_key in groups]
```
在下面的代码中用mapreduce来计算pagerank：

``` Python
# pagerank_mr.py
#
# Computes PageRank, using a simple MapReduce library.
#
# MapReduce is used in two separate ways: (1) to compute
# the inner product between the vector of dangling pages
# (i.e., pages with no outbound links) and the current
# estimated PageRank vector; and (2) to actually carry
# out the update of the estimated PageRank vector.
#
# For a web of one million webpages the program consumes
# about one gig of RAM, and takes an hour or so to run,
# on a (slow) laptop with 3 gig of RAM, running Vista and
# Python 2.5.

import map_reduce
import numpy.random
import random

def paretosample(n,power=2.0):
  # Returns a sample from a truncated Pareto distribution
  # with probability mass function p(l) proportional to
  # 1/l^power.  The distribution is truncated at l = n.

  m = n+1
  while m > n: m = numpy.random.zipf(power)
  return m

def initialize(n,power):
  # Returns a Python dictionary representing a web
  # with n pages, and where each page k is linked to by
  # L_k random other pages.  The L_k are independent and
  # identically distributed random variables with a
  # shifted and truncated Pareto probability mass function
  # p(l) proportional to 1/(l+1)^power.

  # The representation used is a Python dictionary with
  # keys 0 through n-1 representing the different pages.
  # i[j][0] is the estimated PageRank, initially set at 1/n,
  # i[j][1] the number of outlinks, and i[j][2] a list of
  # the outlinks.

  # This dictionary is used to supply (key,value) pairs to
  # both mapper tasks defined below.

  # initialize the dictionary
  i = {}
  for j in xrange(n): i[j] = [1.0/n,0,[]]

  # For each page, generate inlinks according to the Pareto
  # distribution. Note that this is somewhat tedious, because
  # the Pareto distribution governs inlinks, NOT outlinks,
  # which is what our representation is adapted to represent.
  # A smarter representation would give easy
  # access to both, while remaining memory efficient.
  for k in xrange(n):
    lk = paretosample(n+1,power)-1
    values = random.sample(xrange(n),lk)
    for j in values:
      i[j][1] += 1 # increment the outlink count for page j
      i[j][2].append(k) # insert the link from j to k
  return i

def ip_mapper(input_key,input_value):
  # The mapper used to compute the inner product between
  # the vector of dangling pages and the current estimated
  # PageRank.  The input is a key describing a webpage, and
  # the corresponding data, including the estimated pagerank.
  # The mapper returns [(1,pagerank)] if the page is dangling,
  # and otherwise returns nothing.

  if input_value[1] == 0: return [(1,input_value[0])]
  else: return []

def ip_reducer(input_key,input_value_list):
  # The reducer used to compute the inner product.  Simply
  # sums the pageranks listed in the input value list, which
  # are all the pageranks for dangling pages.

  return sum(input_value_list)

def pr_mapper(input_key,input_value):
  # The mapper used to update the PageRank estimate.  Takes
  # as input a key for a webpage, and as a value the corresponding
  # data, as described in the function initialize.  It returns a
  # list with all outlinked pages as keys, and corresponding values
  # just the PageRank of the origin page, divided by the total
  # number of outlinks from the origin page.  Also appended to
  # that list is a pair with key the origin page, and value 0.
  # This is done to ensure that every single page ends up with at
  # least one corresponding (intermediate_key,intermediate_value)
  # pair output from a mapper.

  return [(input_key,0.0)]+[(outlink,input_value[0]/input_value[1])
          for outlink in input_value[2]]

def pr_reducer_inter(intermediate_key,intermediate_value_list,
                     s,ip,n):
  # This is a helper function used to define the reducer used
  # to update the PageRank estimate.  Note that the helper differs
  # from a standard reducer in having some additional inputs:
  # s (the PageRank parameter), ip (the value of the inner product
  # between the dangling pages vector and the estimated PageRank),
  # and n, the number of pages.  Other than that the code is
  # self-explanatory.

  return (intermediate_key,
          s*sum(intermediate_value_list)+s*ip/n+(1.0-s)/n)

def pagerank(i,s=0.85,tolerance=0.00001):
  # Returns the PageRank vector for the web described by i,
  # using parameter s.  The criterion for convergence is that
  # we stop when M^(j+1)P-M^jP has length less than tolerance,
  # in l1 norm.

  n = len(i)
  iteration = 1
  change = 2 # initial estimate of error
  while change > tolerance:
    print "Iteration: "+str(iteration)
    # Run the MapReduce job used to compute the inner product
    # between the vector of dangling pages and the estimated
    # PageRank.
    ip_list = map_reduce.map_reduce(i,ip_mapper,ip_reducer)

    # the if-else clause is needed in case there are no dangling
    # pages, in which case MapReduce returns ip_list as the empty
    # list.  Otherwise, set ip equal to the first (and only)
    # member of the list returned by MapReduce.
    if ip_list == []: ip = 0
    else: ip = ip_list[0]

    # Dynamically define the reducer used to update the PageRank
    # vector, using the current values for s, ip, and n.
    pr_reducer = lambda x,y: pr_reducer_inter(x,y,s,ip,n)

    # Run the MapReduce job used to update the PageRank vector.
    new_i = map_reduce.map_reduce(i,pr_mapper,pr_reducer)

    # Compute the new estimate of error.
    change = sum([abs(new_i[j][1]-i[j][0]) for j in xrange(n)])
    print "Change in l1 norm: "+str(change)

    # Update the estimate PageRank vector.
    for j in xrange(n): i[j][0] = new_i[j][1]
    iteration += 1
  return i

n = 1000 # works up to about 1000000 pages
i = initialize(n,2.0)
new_i = pagerank(i,0.85,0.0001)
```
