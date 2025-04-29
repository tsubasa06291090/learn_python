#文字列

print('Hello') #' ok
print("Hello") #" ok

print("I don't know") #" ' " ok

# pirnt('I don't know') #' ' ' ng
print('I don\'t know') #\でエスケープさせる

print('say "I don\'t know"') # ' が　" を囲んでるからok

# print("say "I don\'t know"") #"でどこからどこまで文字列かわからなくなる ng
print("say \"I don't know\"")

print('Hello.\nHow are you?') #\n で改行

print('C:\name\naem') #\nが邪魔してる
print(r'C:\name\naem') #rawデータのrを先頭につけるといい

#自動で改行されて出力
print("############") # これだと上下に1行ずつ空く
print("""
line1
line2
line3
""")
print("############")

# \をつけることで次の行を読ませるようにする
print("############")
print("""\
line1
line2
line3\
""")
print("############")

print('Hi.' * 3 + 'Mike.') #演算子も使える

#同じ意味
print('py' + 'thon')
print('py''thon')

prefix = 'py'
print(prefix + 'thon') #変数に入れたものは + で繋げる

#同じ意味、文字列長くなると見づらくなるからこうとも書ける
s = ('aaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)
s = 'aaaaaaaaaaaaaaaaaaaaaaaaa' \
    'bbbbbbbbbbbbbbbbbbbbbbbbb'
print(s)