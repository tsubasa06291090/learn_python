# クラスの初期化とクラス変数

class Person(object):
    def __init__(self): # 初期化メソッド、一番最初に呼ばれる
        print('First')
        
    def say_something(self):
        print('hello')
        
# クラスの初期化
person = Person()  # これで __init__ が呼ばれる

# =================

class Person(object):
    def __init__(self, name): # 値を保持するためには self が必要なので、書いておく
        self.name = name  # 値を保持させたい時に self を使う
        print(self.name)
        
    def say_something(self):
        print('hello')

person = Person('Mike') 
# person = Person() # これだとエラーになる。引数が必要な初期化メソッドを定義しているのに、引数なしで呼び出しているため

class Person(object):
    def __init__(self, name='Mike'): # そのため、ここで名前を入れるか
        self.name = name  # 値を保持させたい時に self を使う
        print(self.name)
        
    def say_something(self):
        print('hello')

person = Person('Mike') # ここで名前を入れる

# =================
# self によって保持した値を他の関数で使うことができる
class Person(object):
    def __init__(self, name): 
        self.name = name 
        
    def say_something(self): # self がないと、初期化時に保持した値を使うことができない
        print('I am {}. hello'.format(self.name))  # self.name を使うことで、初期化時に保持した値を使うことができる
        
person = Person('Mike')
person.say_something() # I am Mike. hello

# =================

class Person(object):
    def __init__(self, name): 
        self.name = name 
        
    def say_something(self): 
        print('I am {}. hello'.format(self.name)) 
        self.run()  # 他のメソッドを呼び出すこともできる
    
    def run(self): 
        print('run')
        
person = Person('Mike')
person.say_something() 
# I am Mike. hello
# run
# say_something() の中で run() を呼び出しているので、run() も実行される


class Person(object):
    def __init__(self, name): 
        self.name = name 
        
    def say_something(self): 
        print('I am {}. hello'.format(self.name)) 
        self.run(10)  # 他のメソッドを呼び出すこともできる
        
    # 引数を受け取ることもできる
    # ここでは、run() メソッドに引数 num を設定している
    
    def run(self, num): 
        print('run' * num)  # 引数を受け取ることもできる
        
person = Person('Mike')
person.say_something()  
# I am Mike. hello
# runrunrunrunrunrunrunrunrunrun
# say_something() の中で run(10) を呼び出しているので、run() も実行される
# run() メソッドは、引数 num を受け取っているので、10 回 run の文字列を出力する