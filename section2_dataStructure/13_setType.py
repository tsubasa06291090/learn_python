#集合型

a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a) #uniqueな数だけになってる
print(type(a)) #key: valueの形になってないからtypeはsetになる

b = {2, 3, 3, 6, 7}

print(a)
print(b)
print(a - b) #aとbで重複の数をaから引く
print(b - a)
print(a & b) #論理積、重複したものを返す
# print(a + b) #errorになる
print(a | b) #論理和、重複してる、してない関係なく全てを返す
print(a ^ b) #排他、重複していないものを返す