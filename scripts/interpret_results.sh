#!/bin/bash

HDFS_OUTPUT_DIR=/user/$USER/crime_project/output
LOCAL_OUTPUT_FILE=./output/output.txt

# Create local output directory if it doesn't exist
mkdir -p ./output

# Fetch Hadoop output from HDFS and save to local output.txt
hdfs dfs -cat $HDFS_OUTPUT_DIR/part-* > $LOCAL_OUTPUT_FILE

echo "Fetched results from $HDFS_OUTPUT_DIR to $LOCAL_OUTPUT_FILE"

# Run the interpretation script
python3 src/interpret_results.py
