# 集合内包表記

#list と同じ感じ

s = set()

for i in range(10):
    s.add(i)
    
print(s)

# 集合内包表記
s = {i for i in range(10)}
print(s)

# ========================

s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)
    
print(s)

# 集合内包表記
s = {i for i in range(10) if i % 2 == 0}
print(s)