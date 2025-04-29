d = {'x': 100, 'y':200}

for v in d: #key だけ出力される
    print(v)
    
#key value 両方出力したいとき
for k, v in d.items(): #items: key value を 2 つの変数に取り出せる
    print(k, ':', v)
    
print(d.items()) #list の中に tuple が入った形になっている。そのため、最初の tuple, 次の tuple と順々でアンパッキングされ出力される
