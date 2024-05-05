#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys


def parseLogs():
    """
    Parses logs from standard input and calculates
    the file size and status codes.

    Args:None
    Returns:None
    """
    lineNumber = 0
    fileSize = 0
    statusCodes = {}

    # List of valid HTTP status codes
    codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

    try:
        # Loop through each line in standard input
        for line in sys.stdin:
            lineNumber += 1

            # Split the line into tokens
            tokens = line.split()

            # Check if the line matches the expected format
            if len(tokens) >= 7 and tokens[-2] in codes:
                try:
                    # Extract file size from the last token of the line
                    fileSize += int(tokens[-1])

                    # Increment the count of the status code
                    status_code = tokens[-2]
                    current_count = statusCodes.get(status_code, 0)
                    statusCodes[status_code] = current_count + 1
                except ValueError:
                    # Ignore lines with invalid file size
                    pass

            # If 10 lines have been processed
            # generate report and reset counters
            if lineNumber == 10:
                report(fileSize, statusCodes)
                lineNumber = 0
                fileSize = 0
                statusCodes = {}

        # Generate report for the remaining lines
        if lineNumber > 0:
            report(fileSize, statusCodes)

    except KeyboardInterrupt:
        # Handle keyboard interruption
        report(fileSize, statusCodes)


def report(fileSize, statusCodes):
    """
    Prints generated report to standard output

    Args:
        fileSize (int): total log size after every 10 successfully read lines
        statusCodes (dict): dictionary of status codes and counts
    """
    # Print total file size
    print("Total file size: {}".format(fileSize))

    # Print status codes and their counts in ascending order
    for code in sorted(statusCodes.keys(), key=int):
        print("{}: {}".format(code, statusCodes[code]))


if __name__ == '__main__':
    parseLogs()
