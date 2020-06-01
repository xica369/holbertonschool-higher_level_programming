#!/usr/bin/python3
""" 0. Log parsing
Write a script that reads stdin line by line and computes metrics
"""

import sys
import signal

file_size = 0
http_status = {}
codes_status = ["200", "301", "400", "401", "403", "404", "405", "500"]


def print_logs_formated(file_size, http_status):
    """print_logs_formated"""

    print("File size: {}".format(file_size))
    for key in sorted(http_status):
        print("{}: {}".format(key, http_status[key]))


def signal_handler(sig, frame):
    """signal_handler"""

    print_logs_formated(file_size, http_status)


for index, line in enumerate(sys.stdin, 1):
    if line != "":
        reverted_splitted_line = line.rstrip().split(" ")
        if len(reverted_splitted_line) == 9:
            reverted_splitted_line.reverse()
            file_size += int(reverted_splitted_line[0])
            if reverted_splitted_line[1] in codes_status:
                http_status.setdefault(int(reverted_splitted_line[1]), 0)
                http_status[int(reverted_splitted_line[1])] += 1

        if index % 10 == 0:
            print_logs_formated(file_size, http_status)

        signal.signal(signal.SIGINT, signal_handler)
print_logs_formated(file_size, http_status)
