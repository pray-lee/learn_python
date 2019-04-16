# list = [1, 2, 3, 'leexiaoyong', '中国']
# print(list[3])
# print(list[0:3])

# 增删改查
# 增
# list.append(['1', '2', '3'])
# list.append('lixiaoyong')
# print(list)
#
# list.insert(2, 'insert')
# print(list)
#
# list.extend('二哥') # 添加课迭代的元素，int类型不行
# print(list)

# 删
# list = [1, 2, 3, 4, 5, 6, 7]
# list.pop()  # 按下标删除,
# 如果没有传入参数，默认删除列表最后一项。
# print(list)
# print(list.pop(1), list)
# print(list)
#
# list.remove(5)  # 按元素删除
# print(list)
# list.clear()  #清空列表
# print(list)
# del list  # 从内存中删除
# print(list)

# del list[0:3]  # 切片删除
# print(list)

# 改
# li = ['1', '3', '张三', '李四']
# li[2] = '王五'  # 按索引修改
# print(li)
# li[0:2] = '云姐' # 切片修改(按最小单位)
# print(li)

# 查
# li = [1, 2, 3, 5, 9]
# print(li[0:2])
# print(li[-1]) # 取列表最后一项

# 公共方法
# li = [1, 2, 3, 1, 3]
# print(len(li))
# print(li.count(1))
# print(li.index(3))

# 排序
# li = [1, 5, 3, 4, 8, 1]
# li.sort() # 正向排序
# print(li)
# li.sort(reverse=True) # 反向排序
# print(li)
# li.reverse() # 翻转
# print(li)

# 临时排序
# cars = ['bmw', 'audi', 'toyota', 'subaru']

# print('\nHere is the original list:')
# print((cars))

# print('\nHere is the sorted list:')
# print(sorted(cars))

# print('\nHere is the original list again:')
# print(cars)
