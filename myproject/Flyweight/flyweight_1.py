# flyweight
class User:

  def __init__(self, name='', age=''):
    self.__name = name
    self.__age = age

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, name):
    self.__name = name

  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self, age):
    self.__age = age

  def __str__(self):
    return f'name: {self.__name}, age: {self.__age}'

# flyweightFactory
class UserFactory:

  __instances = {}

  @classmethod
  def get__instance(cls, id):
    if id not in cls.__instances:
      user = User()
      cls.__instances[id] = user
      return user
    return cls.__instances[id]

user1 = UserFactory.get__instance(1)
user2 = UserFactory.get__instance(2)
user3 = UserFactory.get__instance(1)

user1.name = 'taro'
user1.age = 18

print(id(user1))
print(id(user2))
print(id(user3))

print(user1, user3)
