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
num = input('请输入您猜的数字:')

if num == 1:
    print('您猜的是1')
elif num == 2:
    print('您猜的是2')
else:
    print('您猜的是别的')