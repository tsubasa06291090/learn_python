#辞書の使い所

#メニューとその値段を取り出す時に使用すると考える

l = [ #listの場合一から場所を調べて金額を出すプログラムを書かなくてはならない
    ['apple', 100],
    ['banana', 200],
    ['orange', 300],    
]

fruits = { #hash tableの方がvalueを取り出すのが早い
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

print(fruits['apple'])