#!/bin/python3
import sys

def unique_lines(line_arg):
    lines_with_unique_ips = []
    ips = set()
    with open('logs.txt', 'r') as f:
        lines = f.readlines()
        last_lines = lines[-line_arg:]
        for i in last_lines:
            ip = i.split(" ")[1]
            ips.add(ip)
            if ip in ips:
                lines_with_unique_ips.append(i)
    return lines_with_unique_ips

if __name__=='__main__':
    number_last_lines = int(sys.argv[2])
    print(''.join(unique_lines(number_last_lines)))