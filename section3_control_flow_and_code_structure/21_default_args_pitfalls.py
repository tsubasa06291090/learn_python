# デフォルト引数で気をつけること

def test_func(x, l=[]): #list をデフォルト引数にしない
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)

y = [1, 2, 3]
r = test_func(200, y)
print(r)

r = test_func(100)
print(r)
r = test_func(100) 
print(r) # 100 が 2 つ入ったリストができてしまうので、list をデフォルト引数にしてはいけない

"""
list は参照渡しなので、13行目でアクセスした l=[] のアドレスと、
15行目でアクセスした l=[] のアドレスは同じものなので値が追加されるということになる
そのため、dictionary, list などの参照渡しのものは、バグに繋がるのでデフォルト引数にはしない
"""

def test_func(x, l=None): #空の dictionary, list をデフォルトで使用したいときは、 None を代入する
    if l is None:         #もし list が None であれば
        l = []            #l にからの配列を入れる
    l.append(x)
    return l

r = test_func(100)
print(r)
r = test_func(100)
print(r)