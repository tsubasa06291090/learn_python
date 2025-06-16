#文字のメソッド

s ='My name is Mike. Hi Mike.'
print(s)

is_start = s.startswith('My') #startswith: Myで始まってるかどうかの判定
print(is_start)
is_start = s.startswith('X')
print(is_start)

print(s.find('Mike')) #find: 文字列の最初から探して何番目にMikeがあるか
print(s.rfind('Mike')) #rfind: 文字列の最後から探して何番目にMikeがあるか
print(s.count('Mike')) #count: 文字列にMikeが何個あるか
print(s.capitalize()) #capitalize: 文字列の１番最初の文字だけ大文字にする
print(s.title()) #title: 単語ごとに１番最初の文字を大文字にする
print(s.upper()) #upper: すべての文字を大文字に
print(s.lower()) #lower: すべての文字を小文字に
print(s.replace('Mike', 'Nancy')) #replace: 文字列の置き換え