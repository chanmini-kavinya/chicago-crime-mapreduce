#!/usr/bin/env python3
import sys
from collections import defaultdict

def mapper():
    import csv
    reader = csv.reader(sys.stdin)
    for row in reader:
        if row and ("PRIMARY DESCRIPTION" in [col.strip().upper() for col in row]
                    or "LOCATION DESCRIPTION" in [col.strip().upper() for col in row]
                    or (row[0].strip().upper() == 'CASE#')):
            continue
        if len(row) < 7:
            continue
        crime_type = row[4].strip()
        location = row[6].strip()
        if crime_type and location:
            print(f"{crime_type}\t{location}\t1")

def reducer():
    # Use defaultdict to accumulate counts
    counts = defaultdict(int)
    
    # Read and accumulate all counts
    for line in sys.stdin:
        try:
            crime_type, location, count = line.strip().split('\t')
            key = (crime_type, location)
            counts[key] += int(count)
        except (ValueError, IndexError):
            continue
    
    # Output sorted results
    for (crime_type, location), count in sorted(counts.items()):
        print(f"{crime_type}\t{location}\t{count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python3 script.py [mapper|reducer]\n")
        sys.exit(1)
    
    if sys.argv[1] == "mapper":
        mapper()
    elif sys.argv[1] == "reducer":
        reducer()
    else:
        sys.stderr.write("Invalid argument. Use 'mapper' or 'reducer'\n")
        sys.exit(1)


# hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
#     -D stream.num.map.output.key.fields=2 \
#     -D mapred.text.key.partitioner.options=-k1,2 \
#     -D mapred.reduce.tasks=1 \
#     -input /user/$USER/crime_project/chicago_crimes.csv \
#     -output /user/$USER/crime_project/output \
#     -mapper "python3 crime_type_location_count_mapreduce.py mapper" \
#     -reducer "python3 crime_type_location_count_mapreduce.py reducer" \
#     -file crime_type_location_count_mapreduce.py