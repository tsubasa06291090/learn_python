# 標準ライブラリ

# https://docs.python.org/ja/3.13/library/index.html (公式URL)

# 標準ライブラリの中の defaultdict を使ってみる
s = "fjlajfklsdafoegyeiotusdklfjals"

# d = {}
# for c in s:
#     d[c] += 1 # d[] に 0 が入ってないからエラーになる

d = {}
for c in s:
    if c not in d: # d に c がなければ、0 を入れる
        d[c] = 0
    d[c] += 1
print(d)

# =============================

d = {}
for c in s:
    d.setdefault(c, 0) # setdefault: key がなければ何かを入れる。今回の場合は、c がなければ 0 を入れる
    d[c] += 1
print(d)

# =============================
from collections import defaultdict # 標準ライブラリは form や import を使ってあげないとけない <-> 組み込み関数はいらない

d = defaultdict(int) # int のデフォルト、つまり 0 が入る

for c in s:
    d[c] += 1
print(d)
print(d['f'])