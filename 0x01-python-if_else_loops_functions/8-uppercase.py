#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            n = 32
        else:
            n = 0
        print("{:c}".format(ord(str[i]) - n), end='')

