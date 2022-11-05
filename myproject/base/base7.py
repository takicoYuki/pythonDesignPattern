#文字列型

from re import S


fruit = 'apple'

print(fruit)
print(type(fruit))

print(fruit * 10)

new_fruit = fruit + 'banana'

print(new_fruit)

fruit = """apple
banana
grape
"""
print(fruit)

fruit = 'banana'
print(fruit[2])

#encode , decode -> byte[]
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))

#count
msg = 'ABCSDFSDFSDFSWEFW'
print(msg.count('A'))

#strtswith, endswith

print(msg.startswith('A'))
print(msg.endswith('W'))

#strip両端,rstrip右端,lstrip左端
msg = ' ABC '
print(msg)
print(msg.strip())

msg = 'ABCDEGC'
print(msg.strip('C'))
print(msg.lstrip('C'))
print(msg.rstrip('C'))

#upper,lower,swapcase,replace,capitalize
msg = 'abcABC'
msg_u = msg.upper()#大文字
msg_l = msg.lower()#小文字
msg_s = msg.swapcase()#大文字小文字入れ替え
print(msg_u,msg_l,msg_s)

msg = 'ABCDEABC'
msg_r = msg.replace('ABC','FFF',1)
print(msg_r)

msg = 'hello world'
print(msg.capitalize())

#文字列の一部取り出し、format,islower,isupper
msg = 'hello, my name is taro'
print(msg[1:10:1])

print('hello {}'.format('taro'))
name = 'jon'
print(f'hello {name=}') #python3.6以上
print(f'{name=}') #python3.8以上

msg = 'apple'
print(msg.islower())
print(msg.isupper())
m = msg.upper()
print(m)
print(m.isupper())

#find,index,rfind,rindex
msg = 'ABCDEABCD'
print(msg.find('ABC'))#左端から検索
print(msg.rfind('ABC'))#右端から検索
print(msg.index('ABC'))#左端化kら検索
# print(msg.index('AVSDFS')) 見つからないとエラーを吐く
