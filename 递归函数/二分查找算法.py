# 代码实现
def find(l, target, start = 0, end = None):
	end = len(l) if end is None else end
	mid_index = (end-start)//2 + start
	if start <= end:
		if l[mid_index] < target:
			return find(l, target, start = mid_index + 1, end = end)
		elif l[mid_index] > target:
			return find(l, target, start = start, end = mid_index - 1)
		else:
			return mid_index
	else:
			return "没有这个值"

list = [1,2,4,5,6,6,7,8,8,8,9,10,11,25,46,78,9,0,23,45,56,67,9887,10000,12000]
print(find(list, 9887))
print(list.index(9887))

