a = 1
b = 1

#a と b が等しい
print(a == b)
if a == b:
    print('equal')
    
#a と b が異なる
print(a != b)

b = 2
print(a, b)

#a が b よりも小さい
print(a < b)

#a が b より大きい
print(a > b)

a = 2
print(a, b)

#a が b 以下である
print(a <= b)

#a が b 以上である
print(a >= b)

#a も b も真であれば真
print(a > 0 and b > 0)

if a > 0 and b > 0:
    print('a and b are positive')

if a > 0: # and で繋げた方が短くなる
    if b > 0:
        print('a and b are positive')
        
#a または b が真であれば真
a = 1
b = -1

if a > 0 or b > 0:
    print('a or b is positive')
    
a = -1
b = 1

if a > 0 or b > 0:
    print('a or b is positive')

if a > 0: #やはり or を使った方が短くなる
    print('a or b is positive')
elif b > 0:
    print('a or b is positive')