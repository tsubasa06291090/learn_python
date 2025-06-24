# __name__ と __main__

import lesson_package.talk.animal

import config # config.py の print が出力される

print('lesson:', __name__) # __main__ と出力　-> これを実行している main のスクリプトということがわかる

# 合わせて lesson_package/talk/animal.py もみる


# このファイルが他のファイルから読み込まれる場合がある、その場合は以下のようにかく
# ここに書いているのが main の関数だとしても、以下のように書くのが通常のやり方
# ローカルに書いてしまうと実行されてしまうため、python ではこの書き方が良いとされる
def main():
    lesson_package.talk.animal.sing()
    
if __name__ == '__main__':
    main()