#親クラスの継承

class Person:

  def __init__(self,name=str,age=str):
    self.name = name
    self.age = age

  def greeting(self):
    print('hello {}'.format(self.name))

  def say_age(self):
    print('{} years old'.format(self.age))

class Employee(Person): #継承

  def __init__(self, name , age , number):
    super().__init__(name,age)
    self.number = number

  def greeting(self,msg = None): #オーバーライド オーバーロード
    print('I\'m number is = {}'.format(self.number))
    print(msg)

  #pythonではオーバーロードはできない
  #やる場合は引数にデフォルト値Noneを入れて作る

man = Employee('taro','20','00000000000')

man.greeting()
