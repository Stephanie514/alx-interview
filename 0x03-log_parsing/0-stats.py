#!/usr/bin/python3
"""
Script to compute metrics from log lines read from stdin.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
- Total file size: File size: <total size>
- Number of lines by status code:
  possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
  if a status code doesn’t appear or is not an integer, don’t print
  anything for this status code
  format: <status code>: <number>
  status codes should be printed in ascending order
"""

import sys

# Initializing variables to store metrics
total_file_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 7:
            try:
                status_code = int(parts[-2])  # Adjust index to -2
                file_size = int(parts[-1])
                # Updating the metrics
                total_file_size += file_size
                status_counts[status_code] += 1
                line_count += 1
            except (ValueError, IndexError):
                # Skip line if status code or file size is not an integer
                continue

        # Check if the 10 lines have been processed
        if line_count % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code in sorted(status_counts.keys()):
                if status_counts[code] > 0:
                    print("{}: {}".format(code, status_counts[code]))
            print()

except KeyboardInterrupt:
    # Handling keyboard interruption (Ctrl+C)
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))
    sys.exit(0)