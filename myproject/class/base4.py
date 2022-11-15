#instanceMethod staticMethod classMethod

class Human:

  className = 'man' #class変数

  #instanceMethod
  def instanceMethod(self):
    print('instanceMethodを実行')
    print('name = {}'.format(self.className))

  #classMethod
  @classmethod
  def classMethod(cls ,msg):
    print('classMethodを実行')
    print('class変数: name = {} ,msg = {}'.format(cls.className,msg))

  #staticMethod
  @staticmethod
  def staticMethod(msg):
    print('staticMethodを実行')
    print('msg = {}'.format(msg))

#classMethodの呼び出し -> クラス内の変数をとれる
Human.classMethod('hello')

#staticMethodの呼び出し -> 関数に近い
Human.staticMethod('bye')

#instanceMethodの呼び出し
instance_a = Human() #インスタンス化
instance_a.instanceMethod()
