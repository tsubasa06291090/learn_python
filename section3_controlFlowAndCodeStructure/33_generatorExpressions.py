# ジェネレーター内包表記

def g():
    for i in range(10):
        yield i

g = g()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# ========================

# ジェネレーター内包表記
g = (i for i in range(10))
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# ========================

#tuple の場合は
g = tuple(i for i in range(10)) # tuple を () の前に宣言してあげる <- ジェネレーターと間違わないように。
print(type(g))
print(g)

# ========================

# ジェネレーター内包表記
g = (i for i in range(10) if i % 2 == 0)

for x in g:
    print(x)