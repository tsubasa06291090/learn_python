# while else 文

count = 0
while count < 5:
    print(count)
    count += 1
else: #breakで抜けなければ else の方に行く
    print('done')
    
count = 0
while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else: #これだと break でループを抜けるから 'done' は出力されない
    print('done')