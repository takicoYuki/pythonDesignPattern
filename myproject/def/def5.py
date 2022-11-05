#ジェネレータ関数

def gen(max:int):
  print('ジェネレータ作成')
  for n in range(max):
    yield n
    print('yield実行')

generator = gen(10)
# n = next(generator)
# print('n = {}'.format(n))
# n = next(generator)
# print('n = {}'.format(n))
for n in generator:
  print('n = {}'.format(n))
