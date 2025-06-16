# コマンドライン引数

import sys

# 実行例：python 01_command_line_args.py 1 2 3 opthon
print(sys.argv) # プログラムを実行するときの引数をリストにして返す

for i in sys.argv:
    print(i)