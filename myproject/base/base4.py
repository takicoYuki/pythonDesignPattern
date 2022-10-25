#数値型

val = 1
# print(val)

# val = -2
# print(val)

# val = val + 2
# print(val)

# print(val*4)

# print(val/3)

# val = 10
# print(val // 3) #あまりが切り捨て
# print(val % 3)

val += 3 # val = val + 3
# print(val)
# print(val**3)

#浮動小数点数
height = 175.5

print(height)
print(type(height))
#暗黙的キャスト
print(height + 10) #175.5 + 10.0

val = 8
#シフト演算
print(val >> 2)#1000 => 0010
print(val << 3)#1000 => 1000000

print(12 & 21) #01100 and 10101 = 00100 => 4
print(12 | 21) # 01100 or 10101 = 11101 => 29

val = 12
val &= 21 #val = val & 21
print(val)
