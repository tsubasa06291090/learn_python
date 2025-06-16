#数値

import math

print(2 + 2)
print(5 - 2)
print(5 * 6)
print(50 - 5 * 6) #数学と同じように計算される
print((50 - 5) * 6) #優先させたい時は()でくくる
print(8 / 5)

print(type(1)) #int
print(type(1.6)) #float

#どっちも同じ出力
print(0.6)
print(.6)

#割り切れない時はコンピュータの近似値まで表示する
print(17 / 3)
print(17 // 3) #整数部分だけ出力
print(17 % 3 ) #割ったあまり

print(5 ** 2) #冪乗

x = 5
print(x)
y = 10
print(x * y)

pie = 3.1415926535
print(pie)
print(round(pie, 2)) #下2桁で丸める

#math
result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

print(help(math)) #helpを使うとドキュメントが出力される