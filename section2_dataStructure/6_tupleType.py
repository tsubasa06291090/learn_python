#タプル型

t = (1, 2, 3, 4, 1, 2)
print(type(t))

# t[0] = 100 #エラーが起きる
# タブルは値を代入できない

#リストと同じようにスライスやメソッドが使える
print(t[0])
print(t[-1])
print(t[2:5])
print(t)
print(t.index(1))
print(t.index(1, 1))
print(t.count(1))

print(help(list)) #リストを操作するメソッドもある
print(help(tuple)) #count index くらいしかなく、タプルは値を読み込む形の時に使うケースが多い（読み込み専用）

t = ([1, 2, 3], [4, 5, 6])
print(t)

# t[0] = [1] #これだとエラーが起きる、タプルの中のリストを代入しようとすると。
t[0][0] = 100 #タプルの中のリストの中の値に代入することはできる

t = 1, 2, 3 #,をつけた時点でタプルになる
print(type(t))
print(t)
t = 1,
print(type(t))
print(t) #１個しか入ってなくてもカンマがつく

# int と tuple を間違えないように
t = 1
print(type(t)) #int
t = 1,
print(type(t)) #tuple

#これもint, str と tuple を間違えないように
t = ()
print(type(t)) #tuple
print(t)
t = (1)
print(type(t)) #int
print(t)
t = ('test')
print(type(t)) #str
print(t)
t = ('test',) #tupleにするなら必ず,を入れる
print(type(t))
print(t)

# t = 1,
# print(t + 100) #error タプルに値を足すことができない int + tuple になるから

new_tuple = (1, 2, 3) + (4, 5, 6) #このように足すことはできる
print(new_tuple)
x = (1, 2, 3)
y = (4, 5, 6)
print(x + y)

# new_tuple = (1) + (4, 5, 6) #error int + tuple
new_tuple = (1,) + (4, 5, 6) #tupleにするなら必ず,をつける
print(new_tuple)