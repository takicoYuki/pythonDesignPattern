#変数の鷹揚
animal = 'dog'
#変数名に日本語も書けたりする
動物 = 'cat'
print(動物)

#定数は大文字だけで記述する
#決まり事としてらしい
LEGAL_AGE = 20
age = 18


if age < LEGAL_AGE:
    print('未成年')
else:
  print('成人')

#format文
print(f'age={age}') #version 3.6~
print(f'{age=}') #version 3.8~
