# ラムダ

l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun'] # キャピタル（文字の先頭が大文字）が間違えている list があるとする

def change_words(words, func):
    for word in words:
        print(func(word))
        
def sample_func(word):
    return word.capitalize()

change_words(l, sample_func) # sample_func() <- ここで実行したものではなく、sample_func <- オブジェクトを渡す

# ラムダを使ってもう少し簡単に書く
def change_words(words, func):
    for word in words:
        print(func(word))
        
sample_func = lambda word: word.capitalize() # lambda 引数: 処理、という文法になっている。単純な2行程度の func なら lambda を使った方がいい

change_words(l, sample_func)

# 直接 lambda を書く
# ラムダを使ってもう少し簡単に書く
def change_words(words, func):
    for word in words:
        print(func(word))
        
change_words(l, lambda word: word.capitalize())

# lambda を使わないと行数がつらつらと長くなるが、lambda を使うことで短く収まる
def sample_func(word):
    return word.capitalize()

def sample_func(word):
    return word.lower()

change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lowerzz())