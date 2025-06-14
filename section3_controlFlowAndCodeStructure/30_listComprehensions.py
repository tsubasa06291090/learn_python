# リスト内包表記

t = (1, 2, 3, 4, 5)

r = []
for i in t:
    r.append(i)
    
print(r)

# リスト内包表記
r = [i for i in t] # 「for i in t」を一番最初の「i」に追加しているイメージ
print(r)

# ========================

r = []
for i in t :
    if i % 2 == 0:
        r.append(i)
        
print(r)

# リスト内包表記
r = [i for i in t if i % 2 == 0] # 1行で書ける、メモリの使用量が少ないと言われている
print(r)

# ========================

t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    for j in t2:
        r.append(i * j)
        
print(r)

# リスト内包表記
r = [i * j for i in t for j in t2] # 「for i in t」を一番最初の「i」に、「for j in t2」を一番最初の「j」に追加しているイメージ
print(r)

# リスト内包表記は for などの処理が長くない場合に有効。処理が長いと可読性が低くなるため。