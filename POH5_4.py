# coding: utf-8

import sys

#縦、横、選択範囲の総数
x, y, N = sys.stdin.readline().rstrip().rsplit(" ")

#取得した整数格納用と選択範囲の記録用テーブルの宣言
number_table = [[0] * int(x)] * int(y)
selected_table = [[0] * int(x)] * int(y)


input_number_list = sys.stdin.readline().rstrip().rsplit(" ")
