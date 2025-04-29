#リスト型

l = [1, 20, 4, 50, 2, 1, 2]
print(l)
print(l[0])
print(l[1])
print(l[-1]) #最後から１番目
print(l[-2]) #最後から２番目

print(l[0:2])
print(l[:2]) #２番目まで
print(l[2:5])
print(l[2:]) #３番目から最後まで
print(l[:]) #全部

print(len(l)) #len: リストの長さを返す
print(type(l))

print(list('abcdefg')) #str -> list 一文字ずつlistになる

# print(l[100]) #index error 100番目がないから

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
print(n[::2]) #１つ飛ばしで返す
print(n[::3]) #２つ飛ばしで返す
print(n[::-1]) # 最後から順に返す

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x) #ネストを返す、ネスト：リストの中にリストがあること
print(x[0]) #aを取り出す
print(x[1]) #nを取り出す
print(x[0][1]) #'b'を取り出す
print(x[1][2]) #3を取り出す
print(x[-1][-1])