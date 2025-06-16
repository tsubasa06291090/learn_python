# None を判定する場合

is_empty = None #python では何も入っていないものを None とする。変数宣言はしたいけど、何も入れたくない時に使用
print(is_empty) 
print(help(is_empty)) 

if is_empty == None: #等式で None を判定するのは勧められていない
    print('None!')
    
if is_empty is None: #is: 変数は None ですか？という時に使う
    print('None!')
    
if is_empty is not None: #not をこうとも使える
    print('None!')
else:
    print('is not None')
    
print(1 == True) #値を１として真同士だから True
print(1 is True) #オブジェクト同士が同じであると認識しなければ真とはならないため、False
print(True is True) #ok
print(None is None) #ok

#is は None の時に一番使う