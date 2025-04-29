#文字列のインデックスとスライス

word = 'python'
print(word[0]) #１番目の文字を出力
print(word[1])
print(word[-1]) #最後の文字を出力
print(word[-2])
# print(word[100]) #100番目の文字はないからエラー

#スライス
print(word[0:2])
print(word[2:5])

#同じ意味
print(word[0:2])
print(word[:2]) #最初から２番目まで

print(word[2:]) #３番目から最後まで
print(word[:]) #全部出力

# word[0] = 'y' #これだとエラーが起きる
# print(word)
word = 'j' + word[1:] #１番目変更してそれ以降をコピーしてくっつける
print(word)

n = len(word) #len で indexの長さを数える
print(n)