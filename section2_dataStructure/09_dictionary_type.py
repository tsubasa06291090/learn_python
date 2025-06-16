#辞書型

d = {'x': 10, 'y': 20} # key: value の関係
print(d)
print(type(d)) #dict型
print(d['x'])
print(d['y'])

d['x'] = 100 #値の変更
print(d)
d['x'] = 'XXXX'
print(d)
d['z'] = 200 #辞書の追加
print(d)

d[1] = 10000 #数字もkeyになる
print(d)

#色々な書き方
print(dict(a=10, b=20))
print(dict([('a', 10), ('b', 20)])) #listとtuple