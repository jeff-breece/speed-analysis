import matplotlib.pyplot as plt
import numpy as np
import datetime
import re

# Initialize list to hold download speeds
download_speeds = []

# Open and read the log file
with open('log/wifi_speed.log', 'r') as file:
    for line in file:
        # Skip empty lines and error lines
        if not line.strip() or 'Error' in line:
            continue

        try:
            # Use regex to extract download speed
            match = re.match(
                r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}), Ping: ([\d.]+) ms, '
                r'Download: ([\d.]+) Mbit/s, Upload: ([\d.]+) Mbit/s',
                line
            )
            if match:
                download = float(match.group(3))
                download_speeds.append(download)
        except Exception as e:
            print(f"Error parsing line: {line}")
            print(e)

# Define the bins for 50 Mbps groupings
max_speed = max(download_speeds)
bins = np.arange(0, max_speed + 50, 50)

# Calculate the histogram
hist, bin_edges = np.histogram(download_speeds, bins=bins)

# Calculate percentages
total_measurements = len(download_speeds)
percentages = (hist / total_measurements) * 100

# Prepare labels for the bins
bin_labels = [f'{int(bin_edges[i])}-{int(bin_edges[i+1])} Mbps' for i in range(len(bin_edges)-1)]

# Plotting
plt.figure(figsize=(12, 7))
bars = plt.bar(bin_labels, percentages, color='skyblue')

# Add percentage labels above each bar
for bar, percentage in zip(bars, percentages):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f'{percentage:.1f}%', ha='center', va='bottom')

plt.title('Download Speed Distribution in 50 Mbps Bins')
plt.xlabel('Download Speed Range (Mbps)')
plt.ylabel('Percentage of Measurements (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()