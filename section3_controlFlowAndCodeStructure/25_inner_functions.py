# 関数内関数

def outer(a, b):
    print(a, b)
    
outer(1, 2)

def outer(a, b):
    
    def plus(c, d):
        return c + d
    
    r = plus(a, b)
    print(r)
    
outer(1, 2)

def outer(a, b):
    
    def plus(c, d): # 他の関数で使用されない時, かつこの関数内でたくさん使う時に、関数内関数を使う
        return c + d
    
    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)
    
outer(1, 2)