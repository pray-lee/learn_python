# 元祖，只读列表，可循环查询，可切片
# 儿子不能改，孙子可能可以改

tu = (1,2,3,'alex',[2,3,4,'taibai'], 'egon')
print(tu[3])
print(tu[0:4])
tu[4][3] = tu[4][3].upper()
print(tu)
for i in tu:
    print(i)

# s = 'asdf'
# print('---'.join(s))
#
# li = ['1', '2', '3']
# print('---'.join(li))


for i in range(0, 100, 3):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(0, 10, -1):
    print('hah', i)     # 不会报错，也不会输出
