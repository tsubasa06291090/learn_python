# import する際の記述の仕方

# import collections, sys, os ... # 続けて書くことはできるが推奨されていない

# 1行1行書いていく
# import collections
# import sys
# import os

# また、アルファベット順に書く方が読みやすいと言われている
# import collections
# import os
# import sys

"""
・標準ライブラリ, 
・サードパーティライブラリ, 
・自分たちが作成したパッケージ, 
・ローカルのファイル
の間に1行空けるのが良いとされる。それぞれの区別がつくから

この順番でかく
それぞれの区別ないでアルファベット順に書く
"""

import collections
import os
import sys

import termcolor # site-package の中に作られる

import lesson_package

import config

# import するファイルがどこにあるのかを確認する
print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

# python がどこから読み取るかを確認する
# 表示された順に、パッケージとして読み込まれる。
# また、この中にあればパッケージとして読み込むことができる。
# 上から読み込まれるので、上と下に同じパッケージがあるときは、上にある方が優先されて読み込まれる。
print(sys.path) 