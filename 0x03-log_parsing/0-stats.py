#!/usr/bin/python3
"""
Prints metrics based on input from stdin
"""
import sys

stats = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total, counter = 0, 0


def print_metrics():
    """Prints the metrics"""
    print(f'File size: {total}')

    for key, value in sorted(stats.items()):
        if value != 0:
            print(f'{key}: {value}')


try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) == 9:
            try:
                code, size = parts[-2], int(parts[-1])
                if code in stats:
                    stats[code] += 1
                total += size
                counter += 1
            except (IndexError, ValueError):
                continue

        if counter == 10:
            print_metrics()
            counter = 0

except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)

print_metrics()
