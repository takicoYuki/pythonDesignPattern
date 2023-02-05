
from abc import ABC, abstractclassmethod

class Shape(ABC):

  def __init__(self, width, height):
    self._width = width
    self._height = height

  @abstractclassmethod
  def create_shape_str(self):
    pass

class RectangleShape(Shape):

  def __init__(self, width, height):
    super().__init__(width, height)

  def create_shape_str(self):
    rectangle = '*' * self._width + '\n'
    for _ in range(self._height - 2):
      rectangle += '*' + ' ' * (self._width -2) + '*' + '\n'
    rectangle += '*' * self._width + '\n'
    return rectangle

class SquareShape(Shape):

  def __init__(self, width, height = None):
    super().__inti__(width,width)

  def create_shape_str(self):
    rectangle = '*' * self._width + '\n'
    for _ in range(self.width - 2):
      rectangle += '*' + ' ' * (self._width -2) + '*' + '\n'
    rectangle += '*' * self._width + '\n'
    return rectangle

class WriteAbstraction(ABC):

  def __init__(self, shape:Shape):
    self._shape = shape

  def read_shape(self):
    return self._shape.create_shape_str()

  @abstractclassmethod
  def write_to_text(self, file_name):
    pass

class WriteShape(WriteAbstraction):

  def write_to_text(self, file_name):
    with open(file_name, mode='w', encoding='utf-8') as fh:
      fh.write(self.read_shape())


rectangle = RectangleShape(10, 5)
writeShape = WriteShape(rectangle)
writeShape.write_to_text('tmp.txt')
