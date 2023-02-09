from abc import ABC, abstractclassmethod

# Element
class ItemElement(ABC):

  @abstractclassmethod
  def accept(self, visit):
    pass

# ConcreteElement
class Book(ItemElement):

  def __init__(self, price, isbn):
    self.__price = price
    self.__isbn = isbn

  @property
  def price(self):
    return self.__price

  @property
  def isbn(self):
    return self.__isbn

  def accept(self, visitor):
    return visitor.visit(self)

class Fruit(ItemElement):

  def __init__(self, price, weight, name):
    self.__price = price
    self.__weight = weight
    self.__name = name

  @property
  def price(self):
    return self.__price

  @property
  def weight(self):
    return self.__weight

  @property
  def name(self):
    return self.__name

  def accept(self, visitor):
    return visitor.visit(self)

# Visitor
class Visitor(ABC):

  @abstractclassmethod
  def visit(self, item: ItemElement):
    pass

# ConcreteVisitor
class ShoppingVisitor(Visitor):

  def visit(self, item: ItemElement):
    if isinstance(item, Book):
      cost = item.price
      if cost >= 50:
        cost -= 10
      print(f'Book ISBN: {item.isbn}, const = {cost}')
      return int(cost)
    elif isinstance(item, Fruit):
      cost = item.price + item.weight
      cost = cost * 0.8
      print(f'Fruit name: {item.name} cost = {cost}')
      return int(cost)

def calcurate_price(item):

  visitor = ShoppingVisitor()
  sum = 0
  for item in items:
    sum += item.accept(visitor)
  return sum


items = [
  Book(20, '1111'),
  Book(100, '2222'),
  Fruit(8, 10, 'Banana'),
  Fruit(10, 5, 'Apple')
]

# 条件
# Bookは50円以上の場合は、10円引き
# Fruitは20%OFF
print(f'Total cost = {calcurate_price(items)}')
