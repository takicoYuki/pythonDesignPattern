#デフォルト値　可変長引数　複数戻り値

def sample(arg1,arg2 = 100):
  print('arg1 = {},arg2 = {}'.format(arg1,arg2))

sample(1)

def spam1(arg1,*arg2):
  print('arg1 = {} arg1_type = {} ,arg2 ={} arg2_type = {}'.format(arg1,type(arg1),arg2,type(arg2)))

spam1(1,1,1,1,1,1,1,1,1,111,11111)

def spam2(arg1,**arg2):
  print('arg1 = {} arg1_type = {} ,arg2 ={} arg2_type = {}'.format(arg1,type(arg1),arg2,type(arg2)))

spam2(1,name='taro',age=20)

def spam3(arg1,*arg2,**arg3):
  print('arg1 = {} arg1_type = {} ,arg2 ={} arg2_type = {} , arg3 ={} arg3_type = {}'.format(arg1,type(arg1),arg2,type(arg2),arg3,type(arg3)))

spam3(1,234234235,2342342,name ='taro',age = 20)

def sample():
  return 1,2,3

a,b,c = sample()
print('a = {},b = {},c = {}'.format(a,b,c))
