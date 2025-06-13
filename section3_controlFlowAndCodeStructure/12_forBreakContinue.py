# for 文と break 文と continue 文

some_list = [1, 2, 3, 4, 5]

#while 文で全部出力する
i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1
    
#for 文で書くと
for i in some_list: #list の頭から一つずつ引っ張り出される
    print(i)
    
for s in 'abcde': #文字列の頭から1文字ずつ引っ張り出させる
    print(s)
    
for word in ['My', 'name', 'is', 'Mike']:
    print(word)
    
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        break #for でも break が使える
    print(word)
    
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue #for でも continue が使える
    print(word)