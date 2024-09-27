import subprocess
import datetime
import time

def log_speed():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    max_retries = 3
    retry_delay = 10  # seconds

    for attempt in range(max_retries):
        try:
            # Run the speedtest-cli command and capture the output
            result = subprocess.run(['speedtest-cli', '--simple'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            if result.returncode == 0:
                # Parse the output lines
                lines = result.stdout.strip().split('\n')
                ping = lines[0].split(' ')[1]  # Extract the ping value
                download = lines[1].split(' ')[1]  # Extract the download speed
                upload = lines[2].split(' ')[1]  # Extract the upload speed

                # Format the log entry
                log_entry = f"{timestamp}, Ping: {ping} ms, Download: {download} Mbit/s, Upload: {upload} Mbit/s\n"
                break
            else:
                raise Exception(result.stderr.strip())

        except Exception as e:
            log_entry = f"{timestamp}, Error: {e}\n"
            if attempt < max_retries - 1:
                time.sleep(retry_delay)  # Wait before retrying
            else:
                break  # After max retries, don't attempt again

    # Write the log entry to a file
    with open("/home/jeff/src/scripts/speedtest/log/wifi_speed.log", "a") as log_file:
        log_file.write(log_entry)

if __name__ == "__main__":
    log_speed()