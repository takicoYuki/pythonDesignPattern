# prototype

from abc import ABC,abstractclassmethod
from copy import deepcopy

class Prototype(ABC):

  @abstractclassmethod
  def use(self,msg):
    pass

  @abstractclassmethod
  def _clone(self):
    pass


class MessageBox(Prototype):

  def __init__(self,decoration_char):
    self.__decoration_char = decoration_char

  def use(self,msg):
    str_msg = str(msg)
    print(self.__decoration_char * (len(str_msg) + 4))
    print(self.__decoration_char + ' ' + str_msg  + ' ' + self.__decoration_char)
    print(self.__decoration_char * (len(str_msg) + 4))

  def _clone(self):
    print('MessageBoxのクローンを作成します')
    return deepcopy(self)

  @property
  def decoration_char(self):
    return self.__decoration_char

  @decoration_char.setter
  def decoration_char(self,decoration_char):
    self.__decoration_char = decoration_char

class UnderLinePen(Prototype):

  def __init__(self,Underline_char):
    self.__underline_char = Underline_char

  def use(self,msg):
    str_msg = str(msg)
    print(str_msg)
    print(self.__underline_char * len(str_msg))

  def _clone(self):
    print('UnderLinePenのコピーを作成します')
    return deepcopy(self)

  @property
  def underline_char(self):
    return self.__underline_char

  @underline_char.setter
  def underline_char(self,underLine_char):
    self.__underline_char = underLine_char

# インスタンスを管理するManager
class Manager:

  def __init__(self):
    self.__products = {}

  def register(self,name,prototype:Prototype):
    self.__products[name] = deepcopy(prototype)

  def create_product(self,name):
    product = self.__products.get(name)
    return product._clone()


manager = Manager()

m_box = MessageBox('*')
m_box.use('Hello')
u_pen = UnderLinePen('-')
u_pen.use('Hello')

# インスタンスを登録
manager.register('message_box',m_box)
manager.register('underline_pen',u_pen)

# 複製
new_m_box = manager.create_product('message_box')
new_m_box.use('Hello')
