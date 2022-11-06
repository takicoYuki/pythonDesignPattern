#サブジェネレーター

from __future__ import nested_scopes
from re import sub


def sub_sub_generator():
  #yieldで呼び出しもとに返す
  yield "sub sub のyield"
  #一つ上のジェネレーターに値を返す
  return "sub sub のreturn"

def sub_generator():
  #yieldで呼び出しもとに返す
  yield "sub のyield"
  #サブジェネレーター内でサブジェネレーターを呼び出す
  res = yield from sub_sub_generator()
  print("sub res = {}".format(res))
  #一つ上のジェネレーターに値を返す
  return "sub のreturn"

def generator():
  yield "generatorのyield"
  res = yield from sub_generator()
  print("generator res = {}".format(res))
  return "generator のreturn"

gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
