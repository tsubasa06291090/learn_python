# 例外処理

l = [1, 2, 3]
i = 5

# try-except 文: 「try:」 の中で exception が起きたら 「except:」 の部分を実行する。プログラムが実行されづつける。
try:
    l[i]
except:
    print("Don't worry")
    
print("last")

# ========================

try:
    l[i]
except IndexError: # IndexError　が出た時だけ次の行を実行する
    print("Don't worry")
    
print("last")

# ========================

try:
    l[i]
except IndexError as exc: # IndexError の文を変数に入れる
    print("Don't worry: {}".format(exc))
    
print("last")

# ========================

l = [1, 2, 3]
i = 5
del l # l 変数の削除 

# except は複数設置可能
try:
    l[i] # NameError -> except IndexError: は実行されない
except IndexError as exc: # IndexError の文を変数に入れる
    print("Don't worry: {}".format(exc))
except NameError as exc:
    print(exc)
    
print("last")

# ========================

l = [1, 2, 3]
i = 5

try:
    () + l
except IndexError as exc: # IndexError の文を変数に入れる
    print("Don't worry: {}".format(exc))
except NameError as exc:
    print(exc)
except Exception as exc: # IndexError でも NameError でもないものに Exception がある。 -> しかし、どんなエラーも exeption でキャッチするのは python の書き方ではあまり良くない。
    print("other:{}".format(exc))

print("last")

# ========================

l = [1, 2, 3]
i = 5

# try-ecxept-finally 文
try:
    () + l
except IndexError as exc:
    print("Don't worry: {}".format(exc))
except NameError as exc:
    print(exc)
except Exception as exc: 
    print("other:{}".format(exc))
finally: # エラーが起きても起きなくても、最後に必ずこの行が実行される
    print('clean up')
    
# try:
#     () + l
# finally: # except で処理されなくても出力される
#     print('clean up')
    
# ========================

l = [1, 2, 3]
i = 5

# try-ecxept-else-finally 文
try:
    # () + l
    l[0]
except IndexError as exc:
    print("Don't worry: {}".format(exc))
except NameError as exc:
    print(exc)
except Exception as exc: 
    print("other:{}".format(exc))
else: # 成功した場合のみこれが実行される（except を問題なく抜けた時）
    print('done') 
finally: # エラーが起きても起きなくても、最後に必ずこの行が実行される
    print('clean up')