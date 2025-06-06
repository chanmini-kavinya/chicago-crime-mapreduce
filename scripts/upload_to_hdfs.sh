#!/bin/bash

# Set variables
HDFS_INPUT_DIR=/user/$USER/crime_project/input
LOCAL_INPUT_FILE=./input/chicago_crimes.csv

# Create HDFS input directory if it doesn't exist
hdfs dfs -mkdir -p $HDFS_INPUT_DIR

# Upload the local input CSV file to HDFS
hdfs dfs -put -f $LOCAL_INPUT_FILE $HDFS_INPUT_DIR/chicago_crimes.csv

echo "Uploaded $LOCAL_INPUT_FILE to $HDFS_INPUT_DIR in HDFS."
