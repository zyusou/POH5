# coding: utf-8

number = int(input())
week_list = [0] * 7

for i in range(number):
    index = i % 7
    week_list[index] += int(input())

for i in week_list:
    print(i)
