# if 文

x = -10
if x < 0:
    print('negative') #pythonはindentで区別する、暗黙のルールで4つすベースを空ける

x = 10
if x < 0:
    print('negative')
else:
    print('positive')
    
x = 0
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')
    
x = 10
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('1000000000000') #上から見ていって当てはまるのを実行するから気をつける
elif x == 10:
    print('10')
else:
    print('positive')
    
a = 5
b = 10
if a > 0:
    print('a is positive')
    if b > 0: #if の中にまた if を入れられる
        print('b is positive')
        
# if a > 0:
    # print('a is positive')
    #  if b > 0: #indent を揃えないと error になる
        # print('b is positive')
        