# コンストラクタとデストラクタ

class Person(object):
    def __init__(self, name): # コンストラクタ: オブジェクトが生成されるときに呼び出されるメソッド
        self.name = name 
        
    def say_something(self): 
        print('I am {}. hello'.format(self.name)) 
        self.run(10)  
    
    def run(self, num): 
        print('run' * num)  
        
    # オブジェクトが削除されるときに呼び出されるメソッド
    def __del__(self): 
        print('goodbye')  # デストラクタ: オブジェクトが削除されるときに呼び出されるメソッド、使われなくなった時点で自動的に呼び出される
        
person = Person('Mike')
person.say_something() 

print('=====================') # ここで person オブジェクトは使われなくなるので、__del__() が呼び出される

class Person(object):
    def __init__(self, name): # コンストラクタ: オブジェクトが生成されるときに呼び出されるメソッド
        self.name = name 
        
    def say_something(self): 
        print('I am {}. hello'.format(self.name)) 
        self.run(10)  
    
    def run(self, num): 
        print('run' * num)  
        
    # オブジェクトが削除されるときに呼び出されるメソッド
    def __del__(self): # デストラクタ: オブジェクトが削除されるときに呼び出されるメソッド、使われなくなった時点で自動的に呼び出される
        print('goodbye') 
        
person = Person('Mike')
person.say_something() 

del person  # 明示的にオブジェクトを削除することもできる

print('=====================') # ここで person オブジェクトは使われなくなるので、__del__() が呼び出される