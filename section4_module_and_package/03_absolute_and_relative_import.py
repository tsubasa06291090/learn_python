# 絶対パスと相対パスの Import 

# /lesson_package/talk/ のファイルに、絶対パス、相対パスの Import 書いてあるためそこを確認する

# directory の階層が増えれば . で繋いでいけば良い
from lesson_package.talk import human

print(human.sing())
print(human.cry())