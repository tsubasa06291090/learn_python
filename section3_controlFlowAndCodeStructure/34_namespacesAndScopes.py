# 名前空間とスコープ
"""global 変数に document を追加
Test Test ##########################
"""

animal = 'cat' # グローバル変数

print(animal) # 出力できる

def f(): # 出力できる
    print(animal)
    
f()

# ========================

def f():
    # print(animal) # グローバル変数ではなく、ローカル変数を指そうとして、エラーが起きる
    animal = 'dog' # function 内のローカル変数。
    print('after', animal)
    
f()
print('goobal:', animal)

# スコープ内で宣言すれば、グローバル変数とは違う変数名の変数として、このスコープ範囲の中で扱っているということになる。
# ローカル変数として宣言して使おうとしてるのに、ローカル変数で宣言する前に同じ変数名のグローバル変数を出力しようとすると、ローカルでまだ宣言されてないのでエラーが起きる

# グローバル変数を関数内から書き換える場合
def f():
    global animal # グローバルの animal と宣言してあげる 
    animal = 'dog' # グローバル変数を書き換えているということになる
    print('local', animal)
    
f()
print('local', animal)

# ========================

def f():
    animal = 'dog'
    print('local:', locals()) # locals(): 宣言されているローカル変数を dict 型で出力する function。
    
f()
print('global:', globals()) # globas(): 宣言されているグローバル変数を dict 型で出力する function。どんなものが入っているのか確認したい時はこれで確認する。
# __main__ と書いてあれば、python が一番初めに実行しているスクリプトの関数ということになる

# ========================

def f():
    """Test func doc"""
    print(f.__name__) # 関数の名前
    print(f.__doc__) # document 
    
f()
print('global:',__name__) # __main__ なのは、このファイルが一番最初に実行されるファイルだから