#map関数

from re import M


list_a = [1,2,3,4,5]
#map(関数,リスト等でここをforで回すようなイメージ)
map_a = map(lambda x: x * 2 ,list_a)
for x in map_a:
  print(x)

#辞書で作成
man = {
  'name':'taro',
  'age':'18',
  'country':'Japan'
}

map_b = map(lambda x: x + ',' + man.get(x),man)
for x in map_b:
  print(x)

def calcurate(x,y,z):
  if z == '+':
    return x + y
  elif z == '-':
    return x - y

#map(関数,引数、引数、引数)
map_c = map(calcurate,range(5),[3,3,3,3,3],['+','-','+','-','+'])
for x in map_c:
  print(x)
