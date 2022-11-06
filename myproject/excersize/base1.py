#じゃんけん　勝った場合はループ外、負けた場合3回でループ外、あいこはあいこと表示する

#相手の手を回すジェネレーター
def cp_hands_generator():
  while True:
    yield '1'
    yield '2'
    yield '3'
#勝ちの判定
def judgment(my_hand = str,cp_hand = str):
  if (my_hand == '1' and cp_hand == '2'):
    return True
  elif(my_hand == '2' and cp_hand == '3'):
    return True
  elif(my_hand == '3' and cp_hand == '1'):
    return True
  else:
    return False


#相手が出す手
cp_dict = {
  '1':"グー",
  '2':"チョキ",
  '3':"パー",
}

count = 0
cp_hands = cp_hands_generator()

#実際の処理
while True:
  #入力
  my_hand = input('何を出しますか？ \n 1:グー,2:チョキ,3:パー')
  #入力値判定
  if my_hand not in ('1','2','3'):
    print('誤った入力です')
    continue

  cp_hand = next(cp_hands)

  if(my_hand == cp_hand):
    print('あいこ')
  elif(judgment(my_hand,cp_hand)):
    print('あなたの勝ちです')
    break
  else:
    count += 1
    if count == 3:
      print('あなたの負けです。')
      break
    else:
      print('あなたは{}回負けました。3回まで再チャレンジできます。'.format(count))
      continue
