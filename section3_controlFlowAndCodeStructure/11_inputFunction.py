while True:
    word = input('Enter:') #input: 何か入力したら word 変数に入れる
    if word == 'ok':
        break #'ok' が入力されれば break
    print('next')

while True:
    word = input('Enter:')
    num = int(word)
    if num == 100:
        break #100 が入力されれば break
    print('next')
