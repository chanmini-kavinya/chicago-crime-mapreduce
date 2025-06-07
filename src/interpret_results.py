from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

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

# Plot results

crime_types = [x[0] for x in sorted_crime_totals]
crime_counts = [x[1] for x in sorted_crime_totals]
total = sum(crime_counts)

percentages = [count / total * 100 for count in crime_counts]
threshold = 2

labels = [name if pct >= threshold else '' for name, pct in zip(crime_types, percentages)]

def autopct_format(pct):
    return ('%1.1f%%' % pct) if pct >= threshold else ''

plt.figure(figsize=(8,8))
plt.pie(crime_counts, labels=labels, autopct=autopct_format, startangle=140)
plt.title('Crime Type Proportion')
plt.tight_layout()
plt.savefig('output/crime_type_proportion.png')
plt.close()

location_labels = []
location_counts = []

for crime_type, _ in sorted_crime_totals:
    sorted_locs = sorted(crime_data[crime_type].items(), key=lambda x: x[1], reverse=True)[:3]
    locs = [loc for loc, cnt in sorted_locs] + ['']*(3 - len(sorted_locs))
    counts = [cnt for loc, cnt in sorted_locs] + [0]*(3 - len(sorted_locs))
    location_labels.append(locs)
    location_counts.append(counts)

crime_types = np.array([x[0] for x in sorted_crime_totals])
location_counts = np.array(location_counts)
location_labels = np.array(location_labels)

x = np.arange(len(crime_types))
width = 0.25

plt.figure(figsize=(15, 7))
bars = []
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

for i in range(3):
    bar = plt.bar(x + i*width, location_counts[:, i], width, color=colors[i], label=f'Top {i+1}')
    bars.append(bar)

plt.xticks(x + width, crime_types, rotation=45, ha='right')
plt.ylabel('Number of Reports')
plt.title('Top 3 Locations per Crime Type')
plt.tight_layout()

for i in range(3):
    for j, rect in enumerate(bars[i]):
        height = rect.get_height()
        loc_name = location_labels[j, i]
        if height > 0 and loc_name:
            plt.text(rect.get_x() + rect.get_width()/2, height, loc_name, ha='center', va='bottom', fontsize=8, rotation=90)

plt.savefig('output/summary_top3_locations_per_crime_type.png')
plt.close()
