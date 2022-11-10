#特殊メソッド

class Human:
  #コンストラクタ
  def __init__(self,name,age,number):
    self.name = name
    self.age = age
    self.number = number
  #toString
  def __str__(self):
    return self.name + ',' + self.number
  #==
  def __eq__(self,other):
    return (self.name == other.name) and (self.number == other.number)
  #hash
  def __hash__(self):
    return hash(self.name + self.number)

  def __bool__(self):
    return True if self.age >= 20 else False

man = Human('taro',20,'08000000000')
man2 = Human('taro', 18, '08000000000')
man3 = Human('taro', 18, '09000000000')
man_str = str(man)
print(man)
print(man == man2)

tmp1 = True if hash(man) == hash(man2) else False
tmp2 = True if hash(man) == hash(man3) else False
print('hash man == hash man2  {}'.format(tmp1))
print('hash man == hash man3  {}'.format(tmp1))

if man:
  print('True')
else:
  print('False')

if man2:
  print('True')
else:
  print('False')
