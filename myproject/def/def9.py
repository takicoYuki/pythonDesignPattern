#高階関数

#関数を変数としてリストに入れる
def print_hello():
  print('hello')

def print_goodbye():
  print('goodbye')

list_a = ['aa','bb',print_hello,print_goodbye]
list_a[2]()
list_a[3]()

#関数を引数にする
def print_world(msg):
  print('{} world'.format(msg))

def print_hello_world():
  print('hello_world')

def print_hello(func):
  func('hello')
  return print_hello_world


tmp = print_hello(print_world)
tmp()
