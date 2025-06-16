# ImportError の使い方

try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

utils.say_twice('word')

"""
古いパッケージでも、新しいパッケージでもどちらでも良いとすることができる。

try:
    from ... import [old pkg version]
except ImportError:
    from ... import [new pkg version]
"""