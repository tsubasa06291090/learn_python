# range 関数

#for 文と一緒によく使われる

#0 - 9 までの数字を出力する時
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] #いちいちリストを作って出力するのは面倒
for i in num_list:
    print(i)
    
for i in range(10): #range: 数字まで順に出力してくれる、今回は10まで、つまり 0-9 を出力
    print(i)
    
for i in range(2, 10): #2-10 まで出力
    print(i)
    
for i in range(2, 10, 3): #2-10 までを 3 つ飛ばしで出力
    print(i)

for i in range(10): #10 回実行したい時にも使える
    print('hello')
    
for i in range(10):
    print(i, 'hello')
    
for _ in range(10): #i という変数を使わないときは _ で明示的に変数は使わないよと知らせることができる
    print('hello')