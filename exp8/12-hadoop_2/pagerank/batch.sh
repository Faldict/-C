#/bin/bash

HADOOP_PREFIX = /usr/local/hadoop
command = 'hadoop jar $HADOOP_PREFIX/share/hadoop/tools/lib/hadoop-streaming-2.2.0.jar -files *.py'
mv = 'hadoop fs -mv '
rm = 'hadoop fs -rm -r '
cp = 'hadoop fs -copyToLocal '
function func()
{
    for ((i=1; i<$1+1; i++));
    do
        echo "Processing $i"
        eval "$command -input $2/* -output tempoutput -mapper pagerank_mapper.py -reducer pagerank_reducer.py"
        eval "$rm $2"
        eval "$mv tempoutput $2"
    done
}
func $1 $2
eval "mkdir result"
eval "$cp $2/* result"