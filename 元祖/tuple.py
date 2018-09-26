# 元祖，只读列表，可循环查询，可切片
# 儿子不能改，孙子可能可以改

tu = (1,2,3,'alex',[2,3,4,'taibai'], 'egon')
print(tu[3])
print(tu[0:4])
tu[4][3] = tu[4][3].upper()
print(tu)
for i in tu:
    print(i)
