#ポリモーフィズム

#abstract
from abc import abstractclassmethod,ABCMeta

class Human(metaclass = ABCMeta): #親クラス

  def __init__(self,name):
    self.name = name

  @abstractclassmethod
  def say_something(self):
    pass

  def say_name(self):
    print(self.name)

class Man(Human):

  def say_something(self):
    print('男性: 名前は {}'.format(self.name))

class Woman(Human):

  def say_something(self):
    print('女性: 名前は {}'.format(self.name))

#ポリモーフィズム
num = input('0か1を入力してください')
if num == '0':
  Man('taro').say_something()
elif num == '1':
  Woman('hanako').say_something()
else:
  print('入力が間違って言います,入力された値は{}です'.num)
