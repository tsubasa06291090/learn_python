#f-strings

#Python3.6よりformatではなく、f-stringsが使えるようになった
a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Tsubasa'
family = 'Saito'
print(f'My name is {name} {family}. Watashi ha {family} {name}')
