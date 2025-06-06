#!/usr/bin/env python3
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin)
    next(reader, None)  # Skip header
    for row in reader:
        if len(row) < 7:
            continue
        crime_type = row[4].strip()
        location = row[6].strip()
        if crime_type and location:
            print(f"{crime_type}\t{location}\t1")

if __name__ == "__main__":
    mapper()
