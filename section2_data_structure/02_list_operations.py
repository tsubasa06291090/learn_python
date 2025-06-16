#リストの操作

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)
print(s[0])
s[0] = 'X' #str型ではダメだったが、list型だと書き換え可能
print(s)

print(s[2:5])
s[2:5] = ['C', 'D', 'E'] #３つ分スライスしたから、３つ与えている
print(s)
s[2:5] = ['d', 'e'] #２つのだけ与えた場合は、１つリストが消える
print(s)
s[2:5] = [] #３から５番目までのリストを空にする（消す）
print(s)
s[:] = [] #すべて空にする
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
n.append(100) #append: 最後に付け足す
print(n)
n.insert(0, 200) #insert: index0に200を追加
print(n)
n.pop() #pop: 最後を取り出す
print(n)
n.pop(0) #index0を取り出す
print(n)
del n[0] #del: index0を削除
del n #nのlist自体を削除
# print(n) #error n自体が削除され定義されていないから

n = [1, 2, 2, 2, 3]
n.remove(2) #remove: 初めの２を消してくれる
print(n)
n.remove(2)
n.remove(2)
print(n)
# n.remove(2) #ValueError: 削除する2がもうない

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = a + b #xというリストを新しく作り結合
print(x)
a += b #aのリストそのものに結合
print(a)

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y) #extend: xを拡張してyを付け加える
print(x)