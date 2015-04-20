# coding: utf-8
import sys

input_string = sys.stdin.readline()
result = ""

for i , char in enumerate(input_string):
    if i % 2 == 0:
        result += char

print(result)
