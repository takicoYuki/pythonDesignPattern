#プライベート変数

class Human:

  #プライベート変数
  __human = 'human'

  def __init__(self,name,age):
    self.__name = name
    self.__age = age

  def print_msg(self):
    print('name = {},age = {},__human = {}'.format(self.__name,self.__age,self.__human))

human = Human('taro',20)
#無理やりプライベート変数にアクセスする方法
print(human._Human__name)

print(human.print_msg())
