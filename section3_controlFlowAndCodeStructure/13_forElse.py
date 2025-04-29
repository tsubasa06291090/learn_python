for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
else: #for 文でも else が使える
    print('I ate all!')
    
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break 
    print(fruit)
else: #break で抜けるとここは実行されない
    print('I ate all!')