#デコレーター

from textwrap import wrap


def my_decorator(func):
  def wrapper(*args,**kwargs):
    print('*'*100)
    func(*args,**kwargs)
    print(args)
    print('*'*100)
  return wrapper

@my_decorator
def func_a(*args,**kwargs):
  print('func_aを実行')

func_a(1,2,3,4,5)

@my_decorator
def func_b(*args, **kwargs):
  print('func_bを実行')

func_b(1,2,3,4,5,6,7)
