
# 列表推导式

# list = ['SB%s' % i for i in range(10)]
# print(list)

# 生成器表达式
g = (i for i in range(10))
print(g)  # g是生成器
for i in g:
	print(i)

# 推导式和生成器表达式的不同
 # 括号不一样
 # 返回值不一样 , 不占用内存（生成器表达式）

# eg:
def add(n, i):
	return n + i

def test():
	for i in range(4):
		yield i

g = test()
for n in [1, 10]:
	g = (add(n, i) for i in g)

# for循环分解：
	# g = (add(n, i) for i in g)
	# g = (add(n, i) for i in add(n, i) for i in g)
	# g = (add(10, i) for i in add(10, i) for i in test())
	# for 循环 g 生成器
print('11111')
print(list(g)) # 21 22 23 24
