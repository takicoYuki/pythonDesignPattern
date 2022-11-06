# if 1行 lambda

from distutils.command.config import LANG_EXT


y = 10
x = 2 if y > 0 else 1 #y>0 => 2 else 1
print(x)

lambda_a = lambda x: x*x #引数x 戻り値 x*x
print(lambda_a(10))

lambda_b = lambda x,y,z=5:x*y*z #引数x,y,z 戻り値x*y*z
print(lambda_b(2,4)) #2 * 3 * 5 => 40

#条件付きlambda
lambda_c = lambda x,y :y if x<y else x #if(x<y) => y else => x
print(lambda_c(10,2))
