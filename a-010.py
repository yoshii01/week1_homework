# A-10: サイコロ
    # 下記のコードが期待通り動作するような、dice() 関数を実装
    #  ※ dice()関数は1から6の整数をランダムに返す


import random

dice = [1, 2, 3, 4, 5, 6]

idx = random.randint(1, 5)
print(dice[idx]) 




# import random

# dice = [1, 2, 3, 4, 5, 6]
# # dice = [1, 2, 3, 4, 5, 6]  # 結果リストをまとめて定義する


# print(random.choice(dice)) # 1から6の整数をランダムに出力する
