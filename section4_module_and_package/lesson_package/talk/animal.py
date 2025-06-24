from lesson_package.tools import utils # 絶対パス
# from ..tools import utils # 相対パス <- python ではあまり勧められていない。絶対パスで書くのが好ましい

def sing():
    return 'jfklajkjgklajsklafjkslee'

def cry():
    return utils.say_twice('tuioesjlkfjskldafiheagj')

# print(sing()) # import 先を指定していても、import された時点でこれが実行されてしまう

# print('animal', __name__) # import 先を指定していても、import された時点でこれが実行されてしまう

# import された時に実行はされないけど、テストで実行してみたいときに以下を使う <- import される可能性のあるファイルの場合。
if __name__ == '__main__':
    print(sing())
    print('animal', __name__)