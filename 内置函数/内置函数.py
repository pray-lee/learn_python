# 就是网上那些
l = [1,3 , 2, 4, 7, 5]
l1 = reversed(l)
print(l)
print(list(l1))

# def unique(list):
# 	l = []
# 	for i in list:
# 		if i not in l:
# 			l.append(i)
# 	return l
#
# list = [1,1,3,3,4,4,5,5]
# newL = unique(list)
# print(newL)

# filter

def condition(x):
	return x > 10

filter1 = filter(condition, [1,2,10,11]) # 返回生成器


# map
def my_add(x):
	return x + 1
map1 = map(my_add, [1, 3, 4, 5])
print(tuple(map1))

# zip 拉链方法

zpi1 = zip([1,2,3], ['a','b','c'], {'k':'1', 'v': '2'})
print(list(zpi1))

