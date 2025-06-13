# デコレーター

def add_num(a, b):
    return a + b

print('start')
r = add_num(10, 20)
print('end')

print(r)

# デコレーター: 何かしらの function を実行する前とか後とかに何かやりたい、function に何か機能を付け加えたい時に使用

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def add_num(a, b):
    return a + b

f = print_info(add_num)
r = f(10, 20)
print(r)

# デコレーターをもう少し簡単に書く
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info # @デコレータの関数、とすることでこの関数が実行されるときに、デコレーター関数に行く
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

@print_info # 一度デコレータを設定してしまえば、そのあとは何回でも使える
def sub_num(a, b):
    return a - b

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__) # function の引数で渡した name の値を出力
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# 2つのデコレータを使用する
@print_info # ここで print_more を実行
@print_more # ここで add_num を実行
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# デコレータの順序を逆にする
@print_more # ここで print_info を実行
@print_info # ここで add_num を実行
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)