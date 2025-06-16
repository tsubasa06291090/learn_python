# 関数定義

# say_something() #最初にこうしても定義されてなくて、実行できない

def say_something(): #まず定義してから
    print('hi')
    
say_something() #関数の呼び出し、()のつけ忘れのないように

print(type(say_something)) #function型

f = say_something #変数に入れることもできる
f()

#返り値: 関数を呼び出した後に何かを返してほしい
def say_something():
    s = 'hi'
    return s #return: 返り値

result = say_something() #s = 'hi' が返ってきて result 変数に入る
print(result)

#引数を作る
def what_is_this(color): #color の部分が引数
    print(color)

what_is_this('red')

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"
    
result = what_is_this('red')
print(result)
result = what_is_this('green')
print(result)
result = what_is_this('yellow')
print(result)

#同じ処理は関数にする！
