#リスト内包表記

list_a = (1,2,3,'a',4,'b')

#コピーする
list_b = [x*2 for x in list_a]

print(list_b)

list_c = [x for x in range(1000) if x % 7 == 0]
print(list_c)

#辞書型を使ってみる
dict_a ={
  'a':'Apple',
  'b':'Banana'
}

list_c = [dict_a.get(x) for x in list_a if type(x) == str]
print(list_c)

#ジェネレーター
list_d = (x for x in range(100))
print(type(list_d))
print(list_d)

#タプル
list_e = tuple(x for x in range(100))
print(type(list_e))
print(list_e)

#セット
list_f = {x for x in range(100)}
print(type(list_f))
print(list_f)

def func(n):
  for x in range(2,n):
      if n % x == 0:
        return True
  return False

list_g = [x for x in range(1000) if func(x) == False]
print(list_g)
