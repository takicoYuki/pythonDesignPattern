def print_hello():
  print('Hello World')

print_hello()

def num_max(a :int,b :int):
  print('a = {} , b = {}'.format(a,b))
  if a>b:
    return a
  else:
    return b

num_max(1,10)
