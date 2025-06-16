#キーワード引数の辞書化

def menu(entree='beef', drink='wine'):
    print(entree, drink)

menu(entree='beef', drink='coffee')

def menu(**kwargs): #** でキーワード引数を辞書化する
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)
    
menu(entree='beef', drink='coffee')

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}

menu(**d) #** で展開される（13行目と同じ感じ）、それで8行目の ** で再び辞書化される

#位置引数、タプル化、辞書化を一気にできるが、順序が大切（位置引数、タプル化、辞書化の順番で書く）
def menu(food, *args, **kwargs):
    print(food) #位置引数
    print(args) #タプル化
    print(kwargs) #辞書化
    
menu('banana', 'apple', 'orange', entree='beef', drink='coffee')