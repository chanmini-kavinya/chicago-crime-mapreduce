#!/usr/bin/env python3
import sys

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

    if current_key:
        print(f"{current_key[0]}\t{current_key[1]}\t{current_count}")

if __name__ == "__main__":
    reducer()
