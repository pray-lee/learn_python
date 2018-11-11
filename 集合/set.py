# 集合是可变的数据类型，它里面的元素必须是不可变的数据类型，无序，不重复

# set1 = set({1, 2, 3})
# print(set1)

# 去重
li = [1,2,2,33,33,1,4,5]
set = set(li)
print(set)
li = list(set)
print(li)
