from abc import ABC, abstractclassmethod
from random import randint

# Subject
class Subject(ABC):

  def __init__(self):
    self._number = 0
    self._observers = []

  def attach(self, observer):
    self._observers.append(observer)

  def detach(self, observer):
    self._observers.remove(observer)

  @abstractclassmethod
  def notify(self):
    # Observerを呼び出す処理
    pass

  @abstractclassmethod
  def execute(self):
    pass

# ConcreteSubject
class NumberSubject(Subject):

  def notify(self):
    for observer in self._observers:
      observer.update(self)

  def change_value(self):
    number = self._number
    self._number = randint(0,20)
    print(f'number change from {number} to {self._number}')
    self.notify()

  def execute(self):
    print('Number Subject called')

# Observer
class Observer(ABC):

  @abstractclassmethod
  def update(self, subject: Subject):
    pass

# ConcreteObserver
class GraphObserver(Observer):

  def update(self, subject: Subject):
    print('GraphObserver' + '*' * subject._number)
    subject.execute()

class NumberObserver(Observer):

  def update(self, subject: Subject):
    print('NumberObserver' + str(subject._number))
    subject.execute()

subject = NumberSubject()

graph = GraphObserver()
num = NumberObserver()

subject.attach(graph)
subject.attach(num)
subject.change_value()
