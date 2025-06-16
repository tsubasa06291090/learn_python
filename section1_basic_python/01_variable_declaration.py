#変数宣言

num = 1
name = 'Mike'
is_ok = True

#変数と型の確認
print(num, type(num))
print(name, type(num))
print(is_ok, type(is_ok))

num = name 
print(num, type(num))

num = 1
name = '1'
new_num = int(name) #int型

print(new_num, type(name))