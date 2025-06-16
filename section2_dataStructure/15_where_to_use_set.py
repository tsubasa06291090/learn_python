#集合の使い所

#共通の友達を探す
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

#購入したフルーツの種類を調べる
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f) # list -> set
print(kind) 