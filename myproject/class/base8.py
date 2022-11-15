#メタクラス

class MetaException(Exception):
  pass

#クラスの振る舞いを定義するクラス = メタクラス
class Meta1(type): #type(デフォルトのメタクラス)

  def __new__(metaClass,name,bases,class_dict):
    #metaクラス
    print('metaClass = {}'.format(metaClass))
    #クラス名
    print('name = {}'.format(name))
    #継承しているクラス
    print('bases = {}'.format(bases))
    print('class_dict = {}'.format(class_dict))

    #クラスにmy_varのさせる
    if 'my_var' not in class_dict.keys():
      raise MetaException('my_varを定義して下さい')

    #継承を禁止する finalみたいな使い方
    for base in bases: #ClassA => bases() SubClass => bases(ClassA)
      if isinstance(base,Meta1):
        raise MetaException('継承できません')

    return super().__new__(metaClass,name,bases,class_dict)

class ClassA(metaclass = Meta1):
  a = '123'
  my_var = 'AAA'
  pass

class SubClass(ClassA):
  a = '123'
  my_var = 'AAA'
  pass
