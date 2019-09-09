# 无序列表 不会有重复的元素
set1 = {1, 2, 3, 4, 5}

set2 = {4, 5, 6}

print(set1 - set2) # 求差集 {1,2,3}
print(set2 - set1) # {6}
print(set1 & set2) # 求交集 {4,5}
print(set1 | set2) # 求合集  {1,2,3,4,5}

# 定义一个空集合
set3 = set()
print(type(set3), len(set3)) # 'set' 0