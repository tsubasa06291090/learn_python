for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
    
#list の番号も一緒に出力したい
i = 0
for fruit in ['apple', 'banana', 'orange']: #こうもできるが、、、
    print(i, fruit)
    i += 1
    
for i, fruit in enumerate(['apple', 'banana', 'orange']): #enumurate: i に index を 0 から入れて、その次に list の値を入れてくれる
    print(i, fruit)