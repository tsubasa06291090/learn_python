#位置引数のタプル化

def say_something(word):
    print(word)
    
say_something('Hi!')

def say_something(word, word2, word3): #引数を増やし続けるのは面倒くさい
    print(word)
    print(word2)
    print(word3)
    
say_something('Hi!', 'Mike', 'Nancy') 

def say_something(*args): #変数の前に * をつけるとまとめることができる
    print(args)

say_something('Hi!', 'Mike', 'Nancy') #タプルになって出力される

#なので for ループで回してあげる
def say_something(*args): #*args でタプル化
    for arg in args:
        print(arg)
        
say_something('Hi!', 'Mike', 'Nancy')

#*変数は、普通の引数と一緒に使える
def say_something(word, *args):
    print('word =', word) #'Hi!' は word 引数に入り、それ以降は *args にまとめられる
    for arg in args:
        print(arg)

say_something('Hi!', 'Mike', 'Nancy')

#こうともかける
t = ('Mike', 'Nancy')
say_something('Hi!', *t) #*t でタプルのアンパッキング