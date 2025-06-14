# ジェネレーター

l = ['Goog morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)
    
print('#########################')

def greeting():
    # ジェネレータの場合は、要素を一個一個ジェネレートしていく
    yield 'Good morning' # yield: 産出するという意味。python はジェネレーターと判別する
    yield 'Good afternoon'
    yield 'Good night'
    
for g in greeting():
    print(g)
    
print('#########################')
    
g = greeting()
print(next(g)) # yield 'Good morning' を出力して抜ける
print(next(g)) # yield 'Good afternoon' を出力して抜ける
print(next(g)) # yield 'Good night' を出力して抜ける

print('#########################')

g = greeting()
print(next(g))
print('@@@@@@@@')
print(next(g))
print('@@@@@@@@')
print(next(g))

print('#########################')

def counter(num=10): # ジェネレーターを 10 個作る
    for _ in range(num):
        yield 'run' # ジェネレーターに return はない
        
def greeting():
    yield 'Good morning' 
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
c = counter()

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g)) 

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print('#########################')
    
# ジェネレーターを使用することで、重たい処理を一気にするのではなく、小分けに実行することができる。
def greeting(): # ジェネレーターは、値を覚えている
    yield 'Good morning' # 1回目の処理
    for i in range(1000): # ここから、2回目の処理
        print(i)
    yield 'Good afternoon'
    for i in range(1000): # ここから、3回目の処理
        print(i)
    yield 'Good night'
        
g = greeting()

print(next(g))
print(next(g)) 
print(next(g))

print('#########################')

def greeting(): 
    yield 'Good morning' # 1回目の処理
    yield 'Good afternoon'
    yield 'Good night'
        
g = greeting()

print(next(g))
print(next(g)) 
print(next(g))
print(next(g)) # エラーが出る（次がないから）
