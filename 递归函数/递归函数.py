# 递归函数
	# 默认最大递归深度为996次，这个次数是可以被修改的, 不要随意改变

# import sys
# sys.setrecursionlimit(100)

n = 0
def story():
	global n
	n += 1
	print(n)
	story()
story()
