#クラス変数、インスタンス変数

class SampleA():

  class_val = 'class_val' #クラス変数

  def set_val(self):
    self.instance_val = 'instans_val'  # インスタンス変数

  def print_val(self):
    print('クラス変数 = {}'.format(self.class_val))
    print('インスタンス変数 = {}'.format(self.instance_val))

instance_a = SampleA() #インスタンス化
instance_a.set_val() #インスタンス変数を設定
print(instance_a.instance_val)
instance_a.print_val()

print(SampleA.class_val) #クラスから直接クラス変数を確認
print(instance_a.__class__.class_val) #インスタンスからクラス変数を確認

instance_b = SampleA()
instance_b.set_val()
instance_b.print_val
instance_a.__class__.class_val = 'class val 2'

#クラス変数は同じ変数を見ている
print('instance_a:class_val = {} ,id = {}'.format(instance_a.class_val,id(instance_a.class_val)))
print('instance_b:class_val = {} ,id = {}'.format(instance_b.class_val,id(instance_b.class_val)))

#インスタンス変数はインスタンスごと
instance_a.instance_val = 'instance val 2'
print('instance_a:instance_val = {} ,id = {}'.format(instance_a.instance_val,id(instance_a.instance_val)))
print('instance_b:instance_val = {} ,id = {}'.format(instance_b.instance_val,id(instance_b.instance_val)))
