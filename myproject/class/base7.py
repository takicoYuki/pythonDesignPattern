#多重継承
#呼び出しの違い 継承の場合 super() 多重継承の場合 classA
class classA:

  def __init__(self,a_name):
    self.a_name = a_name

  def print_a_name(self):
    print('class_a name = {}'.format(self.a_name))

  def print_hi(self):
    print('class_a hi')


class classB:

  def __init__(self, b_name):
    self.b_name = b_name

  def print_b_name(self):
    print('class_b name = {}'.format(self.b_name))

  def print_hi(self):
    print('class_b hi')

class newClass(classA,classB):

  def __init__(self,a_name,b_name,name):
    classA.__init__(self,a_name)
    classB.__init__(self,b_name)
    self.newClassName = name

  def print_name(self):
    classA.print_a_name(self)
    classB.print_b_name(self)
    print('newClass name = {}'.format(self.newClassName))

  def print_hi(self): #オーバーライド
    classA.print_hi(self)
    classB.print_hi(self)
    print('newClass hi')

sample = newClass('aClass','bClass','newClass')
sample.print_name()
sample.print_hi()
