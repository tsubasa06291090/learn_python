#タプルの使い所

#３つの選択肢から２つ選択するプログラムがあったとする
chose_from_two = ('A', 'B', 'C')
answer = []
answer.append('A')
answer.append('C')
print(chose_from_two)
print(answer)

chose_from_two = ['A', 'B', 'C']
answer = []
chose_from_two.append('A') #間違ってanswerに入れずにこのリストに入れてしまうかもしれない
chose_from_two.append('C') #この場合だとlistだからそのまま処理される
print(chose_from_two)
print(answer)

chose_from_two = ('A', 'B', 'C')
answer = []
chose_from_two.append('A') #タプルにしておけば間違ってもエラーが出るからいい
chose_from_two.append('C') 
print(chose_from_two)
print(answer)