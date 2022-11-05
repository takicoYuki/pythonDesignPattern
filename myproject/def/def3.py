#グローバル変数

def sample():
  #グローバル変数
  global animal
  animal = 'cat'
  print('animal = {},id ={}'.format(animal,id(animal)))

animal = 'dog'
sample()
print('animal = {},id ={}'.format(animal,id(animal)))
