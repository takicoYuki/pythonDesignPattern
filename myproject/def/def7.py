#generator list memorySize

import sys

list_a = [i for i in range(1000000)]

def generator(max:int):
  i = 0
  for n in range(max):
    yield i
    i += 1
print(sys.getsizeof(list_a))
gen = generator(1000000)
print(sys.getsizeof(gen))
