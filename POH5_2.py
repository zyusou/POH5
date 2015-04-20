# coding: utf-8

import sys

number = int(sys.stdin.readline())
week_list = [0] * 7

for i in range(number):
    index = i % 7
    week_list[index] += int(sys.stdin.readline())

for i in week_list:
    print(i)
