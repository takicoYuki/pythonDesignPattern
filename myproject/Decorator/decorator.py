from abc import ABC, abstractclassmethod

class Component(ABC):

  @abstractclassmethod
  def operation(self):
    pass

# Decorator
class ShowCharComponent(Component):

  def __init__(self, char):
    self.__char = char

  def operation(self):
    print(self.__char * 20)

class ShowDecorator(Component):

  def __init__(self, component: Component):
    self._component = component

class ShowMessage(ShowDecorator):

  def __init__(self, component: Component, msg):
    super().__init__(component)
    self.__msg = msg

  def operation(self):
    self._component.operation() # Componentのメソッド
    print(self.__msg) # ShowMessageのメソッド
    self._component.operation()

# Decorator
class WriteDecorator(Component):

  def __init__(self, component: Component, file_name, msg):
    self._component = component
    self._file_name = file_name
    self._msg = msg

# concreteDecorator
class WriteMessage(WriteDecorator):

  def operation(self):
    self._component.operation()
    with open(self._file_name, mode='w') as fh:
      fh.write(self._msg)

show_component = ShowCharComponent('-')
# show_component.operation()

show_message = ShowMessage(show_component, 'Hello World')
# show_message.operation()

show_writeMessage = WriteMessage(show_message, 'tmp.txt', 'Hallo~')
show_writeMessage.operation()
