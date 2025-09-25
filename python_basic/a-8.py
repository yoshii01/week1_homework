# A-8: リストを要素に持つリスト
    # users_info を使って次のような出力
    # 出力内容
    # Name: Bob, Age: 79
    # Name: Tom, Age: 59
    # Name: Ken, Age: 61

from typing import ItemsView


users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]


# リストの形を横並びに変更し、nameとageに代入し出力
for user in users_info:
    name = user[0]
    age = user[1]


    print(f"Name: {name}, Age: {age}")

