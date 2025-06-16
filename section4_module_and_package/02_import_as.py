# Import 文と AS

# full path で読み込む
# directory 名と .file 名という風になっている
# import lesson_package.utils # lesson_package の utils を取得する

# r = lesson_package.utils.say_twice('hello') 
# print(r)

# ========================

# # module から読み込む
# from lesson_package import utils # lesson_package から utils だけを取得しインポートする

# r = utils.say_twice('hello') # これだと utils モジュールの say_twice 関数だとわかるため良い
# print(r)

# ========================

# from lesson_package.utils import say_twice # lesson_package の utils から say_twice 関数だけを取得

# r = say_twice('hello') # これだとどこの関数なのかわからないから、あまり好ましくない。また、同じ関数名があるかもしれないから、コンフリクトする可能性もある。
# print(r)

# ========================

# module を違う名前で呼び出したい時は、as を使用する

from lesson_package.tools import utils as u # as は module 名が長すぎる時に使用しても良いが、どんな module かわからなくなるため基本使わないようにする。

r = u.say_twice('hello') 
print(r)