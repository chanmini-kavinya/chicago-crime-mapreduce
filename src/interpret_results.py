from collections import defaultdict

crime_data = defaultdict(lambda: defaultdict(int))

with open("output/output.txt") as f:
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

output_lines = []
output_lines.append("=" * 50)
output_lines.append("Total Crime Types (Sorted by Count)")
output_lines.append("=" * 50)
for crime_type, total in sorted_crime_totals:
    output_lines.append(f"{crime_type:<30} {total:>10} crimes")

output_lines.append("\n" + "=" * 50)
output_lines.append("Top 3 Locations per Crime Type")
output_lines.append("=" * 50)
for crime_type, _ in sorted_crime_totals:
    sorted_locs = sorted(crime_data[crime_type].items(), key=lambda x: x[1], reverse=True)[:3]
    output_lines.append(f"\n🔹 {crime_type} (Top 3 Locations):")
    for i, (loc, cnt) in enumerate(sorted_locs, 1):
        output_lines.append(f"   {i}. {loc:<25} {cnt} reports")

# Write to summary file
with open("output/summary.txt", "w") as out_f:
    out_f.write("\n".join(output_lines))

# Also print to console
for line in output_lines:
    print(line)