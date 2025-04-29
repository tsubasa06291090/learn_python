#辞書型のコピー

x = {'a': 1}
y = x #参照渡し
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy() #copy: 値渡しを実現
y['a'] = 1000
print(x)
print(y)
