# coding: utf-8

#縦、横、選択範囲の総数を取得
x, y, N = map(int, input().rsplit())

#取得した整数格納用と選択範囲の記録用テーブルの宣言
# number_table = [[0] * int(x)] * int(y)  <=これは配列一括初期化

#一行ごとにListを生成してList内に格納　=>　テーブルになる
#でもずっと同じテーブルに格納し続けちゃうのでこのままじゃだめ
#number_table = [line.rstrip().rsplit(" ") for line in sys.stdin]

#配列だけ先に宣言
number_table = []
flag_table = [[False for i in range(x)] for j in range(y)]

for i in range(y):
    number_table.append(list(map(int, input().rsplit())))

for i in range(N):
    x1, y1, x2, y2 = map(int, input().rsplit())

    for m in range(y1 - 1, y2):
        for n in range(x1 - 1, x2):
            flag_table[m][n] = True

result = 0

for i in range(y):
    for j in range(x):
        if flag_table[i][j]:
            result += number_table[i][j]

print(result)
