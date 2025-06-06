#!/bin/bash

HDFS_OUTPUT_DIR=/user/$USER/crime_project/output

echo "Raw MapReduce output in HDFS:"
hdfs dfs -cat $HDFS_OUTPUT_DIR/part-*