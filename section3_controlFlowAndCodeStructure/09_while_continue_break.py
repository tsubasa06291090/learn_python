# while 文と continue 文と break 文

count = 0
while count < 5: #count が 5 未満の時にループ
    print(count)
    count += 1 #これがないと条件がずっと成立してしまうので無限ループになる
    
count = 0 
while True: #条件が True なので無限ループ
    if count >= 5:
        break #braak: ループを抜ける、if で判定して break で抜ける
    
    if count == 2:
        count += 1
        continue #continue: ループの一番上に戻る
    
    print(count)
    count += 1