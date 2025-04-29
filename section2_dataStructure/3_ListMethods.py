#リストのメソッド

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3)) #index: 3のindexがどこにあるのか返してくれる
print(r.index(3, 3)) #3をindex3から探してくれる

print(r.count(3)) #count: 3が何個あるのかを返す

if 5 in r: #rに５があれば
    print('exist')

if 100 in r:
    print('exist') #100はないので出力されない

r.sort() #sort: 綺麗に並び替え
print(r)
r.sort(reverse=True) #reverseという引数を与えて、逆から綺麗に並び替え
print(r)
r.reverse() #reverse: 逆から綺麗に並べ替え
print(r)

s = 'My name is Mike.'
to_split = s.split(' ') #空白で区切ってリストに入れる
print(to_split)
to_split2 = s.split('!!!') #存在しないものがあると区切らずにそのままリストに入れる
print(to_split2)

x = ' '.join(to_split) #join: to_splitというリストを空白文字を使って繋げる
print(x)
y = ' ###### '.join(to_split)
print(y)

print(help(list)) #リストのドキュメント