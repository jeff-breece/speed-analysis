import matplotlib.pyplot as plt
import datetime
import re

# Initialize lists to hold the data
timestamps = []
pings = []
downloads = []
uploads = []

# Open and read the log file
with open('log/wifi_speed.log', 'r') as file:
    for line in file:
        # Skip empty lines
        if not line.strip():
            continue

        # Check for error lines and skip them
        if 'Error' in line:
            continue

        try:
            # Use regex to extract data
            match = re.match(
                r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}), Ping: ([\d.]+) ms, '
                r'Download: ([\d.]+) Mbit/s, Upload: ([\d.]+) Mbit/s',
                line
            )
            if match:
                timestamp_str = match.group(1)
                ping = float(match.group(2))
                download = float(match.group(3))
                upload = float(match.group(4))

                # Convert timestamp string to datetime object
                timestamp = datetime.datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')

                # Append data to lists
                timestamps.append(timestamp)
                pings.append(ping)
                downloads.append(download)
                uploads.append(upload)
        except Exception as e:
            print(f"Error parsing line: {line}")
            print(e)

# Plotting
plt.figure(figsize=(15, 10))

# Plot Ping
plt.subplot(3, 1, 1)
plt.scatter(timestamps, pings, color='blue')
plt.title('Internet Speed Over Time - Scatter Plot')
plt.ylabel('Ping (ms)')
plt.grid(True)

# Plot Download Speed
plt.subplot(3, 1, 2)
plt.scatter(timestamps, downloads, color='green')
plt.ylabel('Download Speed (Mbit/s)')
plt.grid(True)

# Plot Upload Speed
plt.subplot(3, 1, 3)
plt.scatter(timestamps, uploads, color='red')
plt.xlabel('Time')
plt.ylabel('Upload Speed (Mbit/s)')
plt.grid(True)

plt.tight_layout()
plt.show()