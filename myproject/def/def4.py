# inner関数 ノンローカル変数
def outer():
  value = 'outer_value'
  def inner():
    nonlocal value
    value = 'inner_value'
    print('inner: value = {} , id = {}'.format (value,id(value)))

  inner()
  print('outer: value = {} , id = {}'.format(value, id(value)))

outer()
