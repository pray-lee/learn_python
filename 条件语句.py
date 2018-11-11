# -*- encoding:utf-8 -*-
# if 格式
#   if 条件:
#       结果

"""
if 5 > 4:
    print(666)
print(777)


if 4 < 3:
    print('go if')
else:
    print('go else')
"""

# 多选
num = str(input('请输入您猜的数字:'))

if num == '1':
    print('您猜的是1')
elif num == '2':
    print('您猜的是2')
else:
    print('您猜的是别的')

# 字符串转数字 int('1234') <1234>
# 数字转字符串 str(1234)   <'1234'>