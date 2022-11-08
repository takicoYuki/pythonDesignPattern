#クラスの定義

class Car:
  """車クラス"""
  #プロパティ
  country = 'Japan'
  year = 2022
  name = "rx-9"

  #selfは自身のを指す
  def print_name(self):
    print('print_nameを実行')
    print(self.name)

#インスタンス化
my_car = Car()
print(my_car)
my_car.print_name()

#リストにクラスを入れる
list_a = [1,2,3,Car]
#インスタンス化
list_a[3]().print_name()

#リストにインスタンスを入れる
list_b = [1,2,3,Car()]
list_b[3].print_name()
