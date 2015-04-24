# coding: utf-8

#表の縦、横、矩形選択範囲の総数を取得
x, y, N = map(int, input().rsplit())

#配列だけ先に宣言
number_table = []
flag_table = [[False for i in range(x)] for j in range(y)]

#数値表の作成
for i in range(y):
    number_table.append(list(map(int, input().rsplit())))

#矩形選択された部分のフラグを立てる
for i in range(N):
    x1, y1, x2, y2 = map(int, input().rsplit())

    for m in range(y1 - 1, y2):
        for n in range(x1 - 1, x2):
            flag_table[m][n] = True

result = 0

#フラグが立っている要素だけ足す
for i in range(y):
    for j in range(x):
        if flag_table[i][j]:
            result += number_table[i][j]

print(result)
