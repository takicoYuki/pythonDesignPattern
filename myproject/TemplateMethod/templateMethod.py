from abc import ABC, abstractclassmethod

# AbstractClass
class AbstractDisplay(ABC):

  def display(self):
    self._open()
    for _ in range(5):
      self._print()
    self._close()
    self._additional_method()

  # メソッド名に_がついてるのはabstractクラス

  @abstractclassmethod
  def _open(self):
    pass

  @abstractclassmethod
  def _print(self):
    pass

  @abstractclassmethod
  def _close(self):
    pass

  # 継承先で実装してもしなくてもいいメソッド
  def _additional_method(self):
    pass

# ConcreteClass
class CharDisplay(AbstractDisplay):

  def __init__(self, character):
    self.__character = character

  def _open(self):
    print('<<', end='')

  def _print(self):
    print(self.__character, end='')

  def _close(self):
    print('>>')

class StringDisplay(AbstractDisplay):

  def __init__(self, msg):
    self.__msg = msg

  def _open(self):
    self.__print_line()

  def __print_line(self):
    print('+' + '-' * len(self.__msg) + '+')

  def _print(self):
    print('-' + self.__msg + '-')

  def _close(self):
    self.__print_line()


c = CharDisplay('*')
c.display()

s = StringDisplay('Hello')
s.display()
