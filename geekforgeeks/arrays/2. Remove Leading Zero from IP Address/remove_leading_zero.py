#!/usr/bin/env python

def remove_leading(ip):
    ip = ip.strip()
    triplets = ip.split('.')
    cleaned = []
    for t in triplets:
        cleaned.append(t.lstrip('0'))
    return '.'.join(cleaned)

if __name__ == '__main__':
    while(1):
        the_ip = raw_input("Enter an ip address:\n\n")
        print('\n')
        print(remove_leading(the_ip))