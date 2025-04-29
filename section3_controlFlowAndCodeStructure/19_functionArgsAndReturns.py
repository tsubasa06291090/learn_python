num: int = 10 #num 変数に int 型の 10 を代入

def add_num(a: int, b: int) -> int: #関数でも同じように引数にもあらかじめ型をつけれる。また、返り値の型も -> int で指定している
    return a + b

r = add_num(10, 20)
print(r)

r = add_num('a', 'b')
print(r) #add_num 関数で int 型を指定しているが、プログラム書く人だけに明示しているだけで、文字列でも実行できる。そこに気をつける