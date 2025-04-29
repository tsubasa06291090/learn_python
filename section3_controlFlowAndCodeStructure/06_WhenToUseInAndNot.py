y = [1, 2, 3]
x = 1

if x in y: #in: 入っているのを調べる
    print('in')
    
if 100 not in y: #not in: 入っていないのを調べる
    print('not in')
    
a = 1
b = 2

if not a == b: #a と b が not の時、だがpythonでnotを使うのは勧められていない
    print('Not equal')
    
if a != b: #こっちの方がわかりやすい
    print('Not equal')
    
if a < b:
    print('a > b')
    
if not a > b: #やはり not は理解しずらい
    print('a > b')

is_ok = True

if is_ok == True: #もう変数でTrueにしているから等号で示さなくて良い
    print('hello')

if is_ok != True: #なので否定する時も等号は使わない
    print('hello')
    
if not is_ok: #bool 否定するときは not を使う
    print('hello')