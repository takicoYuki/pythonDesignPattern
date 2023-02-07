
class FlyweightMixin:

  # インスタンス変数
  _instance = {}

  @classmethod
  def get_instance(cls, *args, **kwargs):
    if (cls, *args) not in cls._instance:
      new_instance = cls(**kwargs)
      cls._instance[(cls, *args)] = new_instance
      return new_instance
    else:
      return cls._instance[(cls, *args)]

class User(FlyweightMixin):

  def __init__(self, name, age):
    self.name = name
    self.age = age

class Car(FlyweightMixin):

  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

# 辞書型で値を渡す
user1 = User.get_instance(1, name = "taro", age = 20)
user2 = User.get_instance(1)
print(id(user1), id(user2))

car = Car.get_instance(brand = "toyota", model = "prius")
print(car.brand)
