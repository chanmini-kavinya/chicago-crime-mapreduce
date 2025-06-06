#!/bin/bash

HDFS_INPUT_FILE=/user/$USER/crime_project/input/chicago_crimes.csv
HDFS_OUTPUT_DIR=/user/$USER/crime_project/output

# Remove previous output directory if it exists jps
hdfs dfs -rm -r -f $HDFS_OUTPUT_DIR

# Run the Hadoop Streaming job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
  -D stream.num.map.output.key.fields=2 \
  -D mapred.text.key.partitioner.options=-k1,2 \
  -D mapred.reduce.tasks=1 \
  -input $HDFS_INPUT_FILE \
  -output $HDFS_OUTPUT_DIR \
  -mapper "python3 mapper.py" \
  -reducer "python3 reducer.py" \
  -file src/mapper.py \
  -file src/reducer.py
