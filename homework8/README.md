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

## PageRank

