# -*- encoding:utf-8 -*-
# 循环
flag = True
count = 1
'''
while flag:
    print(count)
    count = count + 1
    if count > 100:
        flag = False

while count <= 100:
    print(count)
    count = count + 1
'''

s = 'aksldfj'

for i in s:
    print(i)

s = 'fsadf苍井空fklsadf'

if '苍井空' in s:
    print('非法字符')