# クロージャー

def outer(a, b):
    
    def inner():
        return a + b
    
    return inner # function の object を返す。inner() <- これなら実行。inner <- これならまだ実行してない。

print(outer(1, 2)) # inner の object の情報が返ってくる。a + b がまだ実行されてない

f = outer(1, 2) # まだ実行されてない。今実行したくない。何かしらの処理をしてから最終的に、変数に入れた関数を実行したいケースにクロージャーを使用する
r = f() # ここで()がついてようやく実行
print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

# 粗く計算したい時、細かく計算したい時に、値をあらかじめ決めておいて、場合分けして計算できる。
print(ca1(10))
print(ca2(10))