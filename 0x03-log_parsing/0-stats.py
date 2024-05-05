#!/usr/bin/python3
"""script that reads stdin line by line and computes metric
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

# Import necessary modules
import sys


def parseLogs():
    """
    Parses logs from standard input and calculates
    the file size and status codes.

    Args:
        None

    Returns:
        None
    """
    stdin = sys.stdin
    lineNumber = 0
    fileSize = 0
    statusCodes = {}

    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for line in stdin:
            lineNumber += 1
            line = line.split()
            try:

                fileSize += int(line[-1])
                if line[-2] in codes:
                    try:
                        statusCodes[line[-2]] += 1
                    except KeyError:
                        statusCodes[line[-2]] = 1
            except (IndexError, ValueError):
                pass
            if lineNumber == 10:
                report(fileSize, statusCodes)
                lineNumber = 0
        report(fileSize, statusCodes)
    except KeyboardInterrupt as e:
        report(fileSize, statusCodes)
        raise
    except BrokenPipeError:
        # Handle the BrokenPipeError explicitly
        pass


def report(fileSize, statusCodes):
    """
    Prints generated report to standard output

    Args:
        fileSize (int): total log size after every 10 successfully read lines
        statusCodes (dict): dictionary of status codes and counts
    """
    print("File size: {}".format(fileSize))
    for key, value in sorted(statusCodes.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    try:
        # Calling parseLogs
        parseLogs()
    except BrokenPipeError:
        pass
