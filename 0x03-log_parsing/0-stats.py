#!/usr/bin/python3
"""
Log Parsing Script
This script reads from stdin and parses log data to calculate
the total file size and the number of occurrences of each status code.
"""

import sys


def print_stats(file_size, status_codes):
    """Prints the accumulated statistics"""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            status_code = parts[-2]
            file_size = int(parts[-1])

            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
        main()
