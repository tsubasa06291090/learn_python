s = 'aaaaaaaaaaaaaaa' + 'bbbbbbbbbbbb'
print(s)

#式で改行するときは\をつける
s = 'aaaaaaaaaaaaaaa' \
    + 'bbbbbbbbbbbb'
print(s)
s = ('aaaaaaaaaaaaaaa' # これでも良い
    + 'bbbbbbbbbbbb')
print(s)

x = 1 + 1 + 1 + 1 + 1 + 1 \
    + 1 + 1 + 1 + 1 + 1 + 1  
print(x)
x = (1 + 1 + 1 + 1 + 1 + 1
    + 1 + 1 + 1 + 1 + 1 + 1)
print(x)
#1行80文字になったら改行するのがルール