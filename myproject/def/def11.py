#再帰

def sample(num = int):
  if num < 0 :
    return
  else:
    print('num = {}'.format(num))
    sample(num-1)

sample(10)

#フィボナッチ
def fib(n):
  return 1 if n < 3 else fib(n-1) + fib(n-2)

for x in range(1,10):
  print(fib(x))
