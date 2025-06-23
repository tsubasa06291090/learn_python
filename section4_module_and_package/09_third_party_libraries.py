# サードパーティのライブラリ

# https://pypi.org/ (公式URL) <- これに登録して公開もできる

# termcolor を使ってみる
# python3 -m pip install --upgrade termcolor

from termcolor import colored

print('test')

print(colored('test', 'red'))

print(help(colored))