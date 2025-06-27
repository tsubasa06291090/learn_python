# クラスの定義

# s = "flajlfjlasflsjf"
# print(s.capitalize()) # capitalize() は、class のオブジェクトで定義されている

# 人間のオブジェクト
class Person(object): # <- これが暗黙の了解で、クラスの継承もできるということからこの書き方が良いとされる
    def say_something(self):
        print('hello')
        
person = Person() # オブジェクトの完成
person.say_something()

# python3 では (object) はいらない
class Person:
    def say_something(self):
        print('hello')
        
person = Person()
person.say_something()

# または () だけでも良い
class Person():
    def say_something(self):
        print('hello')
        
person = Person()
person.say_something()

# こうともできるが、クラスのメソッドとしてつけた方がオブジェクト指向という意味ではわかりやすい
# def person(name):
#     if name == 'A':
#         print('hello')