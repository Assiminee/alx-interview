#!/usr/bin/python3
"""
Prints metrics based on input from stdin
"""
import sys


def print_stats(size, stat_codes):
    """Prints stats"""
    print('File size: {}'.format(size))

    for key, val in stat_codes.items():
        if val != 0:
            print('{}: {}'.format(key, val))


file_size = 0
stats = {
    '200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
    '404': 0, '405': 0, '500': 0
}

count = 0

try:
    for line in sys.stdin:
        line_parts = line.split()

        if len(line_parts) > 2:
            count += 1

            if count <= 10:
                file_size += int(line_parts[-1])
                code = line_parts[-2]

                if code in stats.keys():
                    stats[code] += 1

            if count == 10:
                print_stats(file_size, stats)
                count = 0

finally:
    print_stats(file_size, stats)
