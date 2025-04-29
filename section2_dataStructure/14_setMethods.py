#集合のメソッド

s = {1, 2, 3, 4, 5}
print(s)
# s[0] #listと違って順番がないからerrorになる
s.add(6) #add: 値を追加する
print(s)
s.add(6) #もう一度6を追加しても集合だから増えない
print(s)
s.remove(6) #remove: 値を削除する
print(s)
s.clear() #clear: 中身を空にする
print(s) #set() と出力、dict型の空と区別するためにこうなる

a = {}
print(type(a)) #dict
print(a) #{} と出力

print(help(set))