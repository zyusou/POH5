# coding: utf-8

import sys

#縦、横、選択範囲の総数を取得
x, y, N = sys.stdin.readline().rstrip().rsplit(" ")

#糞コード
x, y, N = int(x), int(y), int(N)

#取得した整数格納用と選択範囲の記録用テーブルの宣言
# number_table = [[0] * int(x)] * int(y)  <=これは配列一括初期化

#一行ごとにListを生成してList内に格納　=>　テーブルになる
#でもずっと同じテーブルに格納し続けちゃうのでこのままじゃだめ
#number_table = [line.rstrip().rsplit(" ") for line in sys.stdin]


#配列だけ先に宣言（気持ち悪いからもっと良い書き方教えて欲しい）
number_table = []
selected_table = []

for i in range(y):
    #number_table[i] = [line.rstrip().rsplit(" ") for line in sys.stdin]
    number_table.append(sys.stdin.readline().rstrip().rsplit(" "))

for i in range(N):
    selected_table.append(sys.stdin.readline().rstrip().rsplit(" "))

#Todo:  配列に格納した値の整数(int)化
#       選択された範囲をフラグで管理
#       フラグが立っている配列の要素を全部足して出力
