#!/usr/bin/env python

def print_table(num):
    for i in range(1, 11):
        print("%s x %s = %s" % (i, num, i*num))

if __name__ == '__main__':
    while(1):
        number = input("Please enter a number between 1-40")
        print_table(number)
        print("\n")
