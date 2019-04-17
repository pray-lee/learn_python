# range
for value in range(1, 5):
    print(value) # 1,2,3,4

# 使用range创建list
numbers = list(range(1, 5))
print(numbers)

# range指定步长
even_numbers = list(range(2, 11, 2))
print(even_numbers) # 2, 4, 6, 8, 10

# squart
squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)

# 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # 0
print(max(digits))# 9
print(sum(digits))# 45

# 列表解析 (for 循环简化版)
squares = [value**2 for value in range(1, 11)]
print(squares)


# 动手试一试
li = list(range(1, 1000001))
# print(li)
# print(sum(li))
# print(min(li))
# print(max(li))

ra = list(range(1, 21, 2))
for item in ra:
    print(item)

ra1 = list(range(3, 30))
for item in ra1:
    if item % 3 == 0:
        print(item)

ra2 = [item ** 3 for item in range(1, 11)]
print(ra2)
