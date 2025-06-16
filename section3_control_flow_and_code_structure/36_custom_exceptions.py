# 独自例外の作成

# raise IndexError('test error') # 自分でエラーメッセージを作成できる

# 自分のエラークラスを作成したい場合
class UppercaseError(Exception): # Exception を継承。Exception というクラスの名前を UppercaseError という名前に変え、自分なりの Exception を作れる。
    pass # Exception と同じ機能だから pass とかく

def check():
    words =['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper(): # isupper: uppercase なら True を返す
            raise UppercaseError(word) # 自分たちで作ったエラーで開発を進めていくのがやりやすいかも。
        
try:
    check()
except UppercaseError as exc: # 自分たちの作った独自のエラーを、プログラムとして書けるため、開発の上で非常にやりやすい。独自の例外だとわかる。
    print('This is my fault. Go next')
