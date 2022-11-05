#ジェネレータ

#ジェネレータ関数
def gen(max:int):
  print('ジェネレータ開始')
  for n in range(max):
    #値を渡す
    x = yield n
    print('x = {}'.format(x))
    print('ジェネレータの実行')

g = gen(10)
n = next(g)
#sendで値を渡す
#途中で値を入れられる
# g.send(100)

#例外を発生させる
# g.throw(ValueError('Invalid value'))

#途中で終了させる
# g.close()

n = next(g)
