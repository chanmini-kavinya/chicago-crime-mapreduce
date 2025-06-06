from collections import defaultdict

crime_data = defaultdict(lambda: defaultdict(int))

with open("output.txt") as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) != 3:
            continue
        crime_type, location, count = parts
        crime_data[crime_type][location] += int(count)

sorted_crime_totals = sorted(
    ((crime_type, sum(locations.values())) for crime_type, locations in crime_data.items()),
    key=lambda x: x[1],
    reverse=True
)

print("=" * 50)
print("Total Crime Types (Sorted by Count)")
print("=" * 50)
for crime_type, total in sorted_crime_totals:
    print(f"{crime_type:<30} {total:>10} crimes")

print("\n" + "=" * 50)
print("Top 3 Locations per Crime Type")
print("=" * 50)
for crime_type, _ in sorted_crime_totals:
    sorted_locs = sorted(crime_data[crime_type].items(), key=lambda x: x[1], reverse=True)[:3]
    print(f"\n🔹 {crime_type} (Top 3 Locations):")
    for i, (loc, cnt) in enumerate(sorted_locs, 1):
        print(f"   {i}. {loc:<25} {cnt} reports")
