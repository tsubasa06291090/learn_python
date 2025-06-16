# from lesson_package.talk import human
# from lesson_package.talk import animal
from lesson_package.talk import * # 上の二つをまとめて呼び出せる
# * で呼び出すと、今回は talk Directory の __init__.py が読み込まれる
# しかし、どんなモジュールが読み込まれるかわかってない状況で、これを使うケースが多いためあまりオススメされていない、なるべく避ける

print(animal.sing())
print(animal.cry())