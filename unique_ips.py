#!/bin/python3
import sys


def unique_ips(line_arg):
    ips = set()
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        last_lines = lines[-line_arg:]
        for i in last_lines:
            ip = i.split(" ")[1]
            ips.add(ip)
    return list(ips)

if __name__=='__main__':
    number_last_lines = int(sys.argv[2])
    print("\n".join(unique_ips(number_last_lines)))
