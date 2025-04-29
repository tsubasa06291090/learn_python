is_ok = True
if is_ok:
    print('OK!')
else:
    print('No!')
    
is_ok = 1
if is_ok: #1 は True を表す
    print('OK!')
else:
    print('No!')

is_ok = 0 #0 は False を表す
if is_ok:
    print('OK!')
else:
    print('No!')

is_ok = 100300
if is_ok: #何かしらの値が入っていれば True
    print('OK!')
else:
    print('No!')

#文字列はあるか確認する時に使える
is_ok = ''
if is_ok: #空の文字列なので False
    print('OK!')
else:
    print('No!')

is_ok = 'dfjalfjlafjs'
if is_ok: #何か文字があれば True
    print('OK!')
else:
    print('No!')

#listに何か入っているか入っていないかの確認の時にも使える
is_ok = []
if is_ok: #list に入ってないので False
    print('OK!')
else:
    print('No!')

is_ok = [1, 2, 3, 4, 5]
if is_ok: #list に入っているので True
    print('OK!')
else:
    print('No!')

if len(is_ok) > 0: #list に入っているかわざわざこうやって調べなくてもいい
    print('OK!')
else:
    print('No!')
    
#Falseになるのは、0, 0.0, '', [], (), {}, set(), None

is_ok = None
if is_ok:
    print('OK!')
else:
    print('No!')