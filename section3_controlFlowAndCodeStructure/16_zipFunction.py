days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

#頑張ればこう書けるが、ちょっと読みにくい
for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])
    
#便利に書くには、、
for day, fruit, drink in zip(days, fruits, drinks): #zip: それぞれの list の頭から順に出力する。index を指定しなくて済むから可読性がいい
    print(day, fruit, drink)
