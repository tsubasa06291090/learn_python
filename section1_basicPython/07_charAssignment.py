#文字の代入

print('a is {}'.format('a'))
print('a is {} {} {}'.format(1, 2, 3)) #数字も勝手にstr型に変換される

print('a is {0} {1} {2}'.format(1, 2, 3)) #{}にformatのインデックスの指定ができる
print('a is {2} {1} {0}'.format(1, 2, 3))

print('My name is {} {}'.format('Tsubasa', 'Saito'))
print('My name is {0} {1}. Watashi ha {1} {0}'.format('Tsubasa', 'Saito'))
print('My name is {name} {family}. Watashi ha {family} {name}'.format(name='Tsubasa', family='Saito')) # 変数に代入

print(1) #int型
print(str(1)) #str型に変換
x = str(1)
print(type(x))

print(str(3.14)) #float -> str
print(type(str(3.14)))
print(str(True)) #bool -> str
print(type(str(True)))