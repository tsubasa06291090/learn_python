#辞書型のメソッド

d = {'x': 10, 'y': 20}
print(d)
print(help(dict))
print(help(d)) #変数の型でもhelpが読み出せる

print(d.keys()) #keys: keyだけを返す
print(d.values()) #values: valueだけを返す

d2 = {'x': 1000, 'j': 500}
print(d)
print(d2)
d.update(d2) #update: 同じkeyなら上書き、新しいkeyなら追加する
print(d)

#keyがあれば同じように返す
print(d['x'])
print(d.get('x'))

# print(d['z']) #keyがないからエラーが出る
print(d.get('z')) #get: keyがあれば取り出し、なければNoneを返す
r = d.get('z')
print(r)
print(type(r))

print(d)
print(d.get('x')) #getではxの値を取り出せない
print(d)
print(d.pop('x')) #pop: keyのvalueを返し、また取り出す
print(d)

del d['y'] #del: keyとvalueを削除する
print(d)
del d #変数自体を削除してしまうと、
# print(d) #定義されていないため、エラーが起きる
d = {'a': 100, 'b': 200} 
d.clear() #clear: delでの変数ごと削除を予防するために使用、空の辞書になる
print(d)

d = {'a': 100, 'b': 200}
print('a' in d) #in: keyがあるかどうかを判定、あればTrue, なければFalse
print('j' in d)