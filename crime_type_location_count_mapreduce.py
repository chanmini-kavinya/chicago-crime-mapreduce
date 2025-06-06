#!/usr/bin/env python3
import sys

def mapper():
    import csv
    reader = csv.reader(sys.stdin)
    next(reader, None)
    for row in reader:
        if len(row) < 7:
            continue
        crime_type = row[4].strip()
        location = row[6].strip()
        if crime_type and location:
            print(f"{crime_type}\t{location}\t1")

def reducer():
    current_key = None
    current_count = 0

    for line in sys.stdin:
        parts = line.strip().split('\t')
        if len(parts) != 3:
            continue
        crime_type, location, count = parts
        try:
            count = int(count)
        except ValueError:
            continue

        key = (crime_type, location)
        if key == current_key:
            current_count += count
        else:
            if current_key:
                print(f"{current_key[0]}\t{current_key[1]}\t{current_count}")
            current_key = key
            current_count = count

    # Print the last key
    if current_key:
        print(f"{current_key[0]}\t{current_key[1]}\t{current_count}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ['mapper', 'reducer']:
        sys.stderr.write("Usage: python3 crime_type_location_count_mapreduce.py [mapper|reducer]\n")
        sys.exit(1)

    if sys.argv[1] == "mapper":
        mapper()
    else:
        reducer()

# hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
#     -D stream.num.map.output.key.fields=2 \
#     -D mapred.text.key.partitioner.options=-k1,2 \
#     -D mapred.reduce.tasks=1 \
#     -input /user/$USER/crime_project/chicago_crimes.csv \
#     -output /user/$USER/crime_project/output \
#     -mapper "python3 crime_type_location_count_mapreduce.py mapper" \
#     -reducer "python3 crime_type_location_count_mapreduce.py reducer" \
#     -file crime_type_location_count_mapreduce.py

# hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
#   -D stream.num.map.output.key.fields=2 \
#   -D mapred.text.key.partitioner.options=-k1,2 \
#   -D mapred.reduce.tasks=1 \
#   -input /user/$USER/crime_project/chicago_crimes.csv \
#   -output /user/$USER/crime_project/output \
#   -mapper "python3 mapper.py" \
#   -reducer "python3 reducer.py" \
#   -file mapper.py \
#   -file reducer.py


# hdfs dfs -cat /user/$USER/crime_project/output/part-* > output.txt
