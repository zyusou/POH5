# coding: utf-8

string = input()
result = ""

for i , char in enumerate(string):
    if i % 2 == 0:
        result += char

print(result)
