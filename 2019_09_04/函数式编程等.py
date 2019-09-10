# 函数式编程

# 匿名函数    后面只能跟表达式
func = lambda param: param
print(func(1)) # 1


# 三元表达式
# 条件为真的结果  if   条件判断  else   条件为假时的返回结果
# x if x > y else y
x = 1
y = 2
r = x if x > y else y
print(r) # 2

# map 函数
# list_x = [1,2,3,4,5]
# def square(x):
    # return x*x
# result_map = list(map(square, list_x))
# print(result_map)

list_x = [1, 2, 3, 4, 5]
result_map = map(lambda x: x * 8, list_x)
print(list(result_map))


# lambda表达式的参数如果有两个， 就需要传入两个列表与之对应
list_y = [1, 2, 3, 4, 5]
list_z = [1, 2, 3, 4, 5]
result_map1 = map(lambda x, y: x*x + y, list_y, list_z)
print(list(result_map1))



# reduce
from functools import reduce

list_reduce = [1, 2, 3, 4, 5, 6]
result_reduce = reduce(lambda x, y: x + y, list_reduce)
print(result_reduce)
