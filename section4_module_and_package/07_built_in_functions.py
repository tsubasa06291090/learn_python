# 組み込み関数

# https://docs.python.org/ja/3.13/library/functions.html (公式URL)

print(globals()) # builtins module が使われているのがわかる

import builtins
builtins.print()

# 組み込み関数の中の sorted を使ってみる
ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

ranking.get('A') # これで A の value がみれる

print(sorted(ranking, key=ranking.get)) # それぞれの key の value で並び替えを行う。低い順で出力
print(sorted(ranking, key=ranking.get, reverse=True)) # 高い順で出力
