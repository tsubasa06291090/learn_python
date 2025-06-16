# 位置引数とキーワード引数とデフォルト引数

def menu(entree):
    print(entree)
    
menu('beef')

def menu(entree, drink, dessert): #引数を複数つけられる
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

#位置引数
menu('beef', 'beer', 'ice') 
menu('beef', 'ice', 'beer') #引数に入れる順番を間違えないようにする

#間違えないために、キーワード引数を使用する
menu(entree='beef', dessert='ice', drink='beer') #キーワード引数だと順番関係なく指定できる

#位置変数とキーワード引数を一緒に使用
menu('beef', dessert='ice', drink='beer')
# menu(dessert='ice', 'beef', drink='beer') #キーワード引数の後に、位置引数を設置できないため error

#デフォルト引数
def menu(entree='beef', drink='wine', dessert='ice'): #関数にデフォルト引数を指定
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)
    
menu() #引数として何も渡さなかった場合は、関数で指定しているデフォルト引数が呼び出される
menu(entree='chicken') #引数と渡すと、chichen に上書きされて出力される
menu(entree='chichen', drink='beer')
menu('chichen', drink='beer')