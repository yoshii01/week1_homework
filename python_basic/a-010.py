# A-10: サイコロ
    # 下記のコードが期待通り動作するような、dice() 関数を実装
    #  ※ dice()関数は1から6の整数をランダムに返す


# def 関数名1(引数1, 引数2, ...):
#     # 何らかの処理を記述する
#     return 結果
# # 空行1行目
# # 空行2行目
# def 関数名2(引数1, 引数2, ...):
#     # 何らかの処理を記述する
#     return 結果

import random


def dice():
    return random.randint(1, 6)


print(dice())

# import random

# dice = [1, 2, 3, 4, 5, 6]
# # dice = [1, 2, 3, 4, 5, 6]  # 結果リストをまとめて定義する


# print(random.choice(dice)) # 1から6の整数をランダムに出力する


# import random

# dice = [1, 2, 3, 4, 5, 6]

# idx = random.randint(1, 5)
# print(dice[idx]) 
