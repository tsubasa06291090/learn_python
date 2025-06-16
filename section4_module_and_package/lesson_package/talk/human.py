# from lesson_package.tools import utils # 絶対パス
from ..tools import utils # 相対パス <- python ではあまり勧められていない。絶対パスで書くのが好ましい

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')