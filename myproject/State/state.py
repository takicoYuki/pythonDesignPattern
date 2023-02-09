from abc import ABC, abstractclassmethod
from datetime import datetime

# State
class State(ABC):

  @abstractclassmethod
  def begin(self):
    pass

  @abstractclassmethod
  def write_log(self):
    pass

  @abstractclassmethod
  def end(self):
    pass

class DayState(State):

  def begin(self):
    print('昼の処理を開始します')
    self.write_log()
    self.end()

  def write_log(self):
    with open('tmp.txt', mode='w', encoding='utf-8') as fh:
      fh.write('昼のログ')

  def end(self):
    print('昼の処理を修了します')

class NightState(State):

  def begin(self):
    print('夜の処理を開始します')
    self.write_log()
    self.end()

  def write_log(self):
    with open('tmp.txt', mode='w', encoding='utf-8') as fh:
      fh.write('夜のログ')

  def end(self):
    print('夜の処理を修了します')


class Context:

  def __init__(self):
    # デフォルト値
    self.__state = DayState()

  def do(self):
    self.__state.begin()

  def change_state(self, state: State):
    self.__state = state

  def change_state_by_time(self):
    now = datetime.now()
    if(now.hour < 6 ) or (now.hour >= 20):
      self.__state = NightState()
    else:
      self.__state = DayState()


context = Context()
context.change_state(NightState())
context.change_state_by_time()
context.do()
