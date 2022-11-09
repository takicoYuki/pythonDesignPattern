#コンストラクタ

from email.errors import NoBoundaryInMultipartDefect

class SampleA:

  #コンストラクタ
  def __init__(self,msg,name = None):
    print('コンストラクタが呼び出されました')
    self.msg = msg
    self.name = name
  #デストラクタ => 削除時に呼び出される
  def __del__(self):
    print('デストラクタが呼び出されました')
    print('name = {}'.format(self.name))

  def print_msg(self):
    print(self.msg)

  def print_name(self):
    print(self.name)

instance_a = SampleA('Hello','taro')
instance_a.print_msg()
instance_a.print_name()

del instance_a
