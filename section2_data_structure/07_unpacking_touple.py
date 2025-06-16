#タプルのアンパッキング

#アンパッキング：複数の要素を持つデータ構造を分解して、それぞれの要素を個別の変数に代入すること

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple #アンパッキング
print(x, y)

x, y = (10, 20) #これと一緒
print(x, y)
x, y = 10, 20 #タプルはカッコいらないからこうともかける
print (x, y)

min, max = 0, 100 #pythonの場合はタプルを展開して値を入れるという感じ
print(min, max)

#これだと長くてプログラムが見にくい
a, b, c, d, e, f = 'Mike', '1', '1', '1', 'e', 'f'
#２個くらいならいいが長い場合は以下のようにしたほうが読みやすい
a = 'Mike'
b = '1'
c = '1'
d = '1'
e = 'e'
f = 'f'

i = 10
j = 20
print(i, j)
tmp = i
i = j
j = tmp
print(i, j)

a = 100
b = 200
print(a, b)
a, b = b, a #タプルを利用すると一行で入れ替えれる
print(a, b)