# 数据类型划分：可变数据类型和不可变数据类型
# 不可变数据类型：tuple, bool, int, str    可哈希
# 可变数据类型：list, dict, set                 不可哈希
# dict的key必须是不可变数据类型，dict的value可以是任意数据类型

# dict优点： 查询速度快。（二分查找算法） 可存储大量的关系型数据
# dict特点： 无序的,3.6版本以下的是无序的

# 增删改查

# dic1 = {
#     'name': 'leexiaoyong',
#     'mix': [
#         {
#             'haha': 'ssss'
#         }
#     ]
# }

# 增
# dic1['age'] = 88  # 如果没有键，为增加，如果有，则覆盖
# dic1.setdefault('height', 185) # 用的比较少, 他和上面的区别：如果有键，则不进行操作。如果没有，为增加
# print(dic1)

# 删
# dic1.pop('name')  # 有返回值，按键去删除
# dic1.pop('hehe', None)  # 如果不确定有没有这个键，则参数加一个none(可以随意写，一般都写none), 可以设置返回值，这样的话不会报错。如果不设置，则会报错。影响代码的执行
# dic1.popitem()  # 随机删除一个，也有返回值，返回值为一个元祖（包含键和值）
# dic1.clear()  # 清空字典
# del dic1      # 删除字典
# print(dic1)

# 改
# dic = {'name': 'lee', 'age': 80}
# dic2 = {'name': 'zhang', 'weight': 190}
# dic2.update(dic)  # 把dic的内容更新到dic2中，如果dic2中有dic里的键，则dic2里面的键对应的值会被修改，如果没有，则会添加
# print(dic)
# print(dic2)

# 查
# dic3 = {
#     'age': 18,
#     'name': 'lee',
#     'sex': 'male'
# }
# print(dic3.keys())    # 键的集合
# print(dic3.values())  # 值的集合
# print(dic3.items())   # 元祖集合
# 上面三个都可以 for in 循环  并且可以和JS一样，有解构赋值
# for key, value in dic3.items():
#     print(key, value)   # 解构赋值
#
# # 通过get查
# print(dic3.get('age'))       # 如果没有这个值，则会报错
# print(dic3.get('age1', '没有这个值'))   # 如果没有这个值，则会输出后面的消息,不会报错


