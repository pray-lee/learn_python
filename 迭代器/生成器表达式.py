
# 列表推导式

list = ['SB%s' % i for i in range(10)]
print(list)

# 生成器表达式
g = (i for i in range(10))
print(g)  # g是生成器
for i in g:
	print(i)

# 推导式和生成器表达式的不同
 # 括号不一样
 # 返回值不一样 , 不占用内存（生成器表达式）
