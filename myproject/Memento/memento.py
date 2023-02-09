from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import pickle

# Originator
class Originator:

  def __init__(self, state, name):
    self._state = state
    self._name = name

  def change_state(self, new_state):
    print(f'Change State 実行: {new_state}')
    self._state = new_state

  def change_name(self, name):
    print(f'Change Name 実行: {name}')
    self._name = name

  def __str__(self):
    return f'State: {self._state}, name: {self._name}'

  def save(self):
    return ConcreteMemento(self._state, self._name)

  def restore(self, memento):
    self._state = memento.state
    self._name = memento.name
    print(f'Originator: State Change To: {self._state}')

# Memento
class Memento(ABC):

  @abstractclassmethod
  def get_name(self):
    pass

  @abstractclassmethod
  def date(self):
    pass


# ConcreteMemento
class ConcreteMemento(Memento):

  def __init__(self, state, name):
    self._state = state
    self._name = name
    self._date = datetime.now()

  @property
  def state(self):
    return self._state

  @property
  def name(self):
    return self._name

  @property
  def date(self):
    return self._date

  def get_name(self):
    return f'{self._date} / ({self._state})'

# CateTaker
class CateTaker:

  def __init__(self):
    self._mementos = []

  def backup(self, memento: Memento):
    print(f'Originalの状態を保存: {memento.get_name()}')
    self._mementos.append(memento)

  def undo(self):
    if not len(self._mementos):
      # 中身がないときは何も返さない
      return
    # 最後に入れたデータを取得
    memento = self._mementos.pop()
    return memento

  def show_history(self):
    print('変更履歴')
    for memento in self._mementos:
      print(memento.get_name())

# fileにバックアップを保存する
class OriginatorBackup:

  @staticmethod
  def dump_file(originator, file_name):
    with open(file_name, mode='wb') as fh:
      pickle.dump(originator,fh)

  @staticmethod
  def load_file(file_name):
    with open(file_name, mode='rb') as fh:
      return pickle.load(fh)

originator = Originator('FirstState', 'Originator 1')
care_taker = CateTaker()

# バックアップ
backup_instance = originator.save()

# CareTakerに保存
care_taker.backup(backup_instance)

originator.change_state('Second Status')
care_taker.backup(originator.save())

care_taker.show_history()

# OriginatorBackup.dump_file(originator, 'tmp.dump')
originator_backup_dump_file = OriginatorBackup.load_file('tmp.dump')
print(originator_backup_dump_file)
print(type(originator_backup_dump_file))
