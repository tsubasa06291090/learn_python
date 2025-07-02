# クラスの継承

class Car(object):
    pass # 何もしない

class ToyotaCar(Car): # Car クラスを継承して ToyotaCar クラスを定義、クラスを拡張するようなイメージ
    pass

car = Car() # Car クラスのオブジェクトを生成
# 何もしないクラスなので、何も出力されない

# ==========================
class Car(object): # ベースクラスを定義
    def run(self):
        print('run')

class ToyotaCar(Car): # Car クラスを継承して ToyotaCar クラスを定義、クラスを拡張するようなイメージ
    pass

car = Car() # Car クラスのオブジェクトを生成
car.run() # run メソッドを呼び出す

toyota_car = ToyotaCar()
toyota_car.run() # ToyotaCar クラスも Car クラスを継承しているので、run メソッドを呼び出すことができる

# ==========================

class Car(object): # ベースクラスを定義することで、その機能を他のクラスに継承して使うことができる
    def run(self):
        print('run')

class ToyotaCar(Car): # Car クラスを継承して ToyotaCar クラスを定義、クラスを拡張するようなイメージ
    pass

class TeslaCar(Car): # Car クラスを継承して TeslaCar クラスを定義、クラスを拡張するようなイメージ
    def auto_run(self): # TeslaCar クラス独自のメソッドを定義
        # auto_run メソッドは TeslaCar クラスでのみ使用される
        # ただし、Car クラスを継承しているので、run メソッドも使用できる
        print('auto run')
        
tesla_car = TeslaCar()
tesla_car.run() # Car クラスを継承して run メソッドを呼び出すことができる
tesla_car.auto_run() # auto_run メソッドを呼び出すことができる

# ==========================
# もし継承しなかった場合、どのオブジェクトにもrun を定義しなければならない

class Car(object): 
    def run(self):
        print('run')

class ToyotaCar(object):
    def run(self):
        print('run')
        
class TeslaCar(object):
    def run(self):
        print('run')

    def auto_run(self): 
        print('auto run')