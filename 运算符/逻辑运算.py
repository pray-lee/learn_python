# and or not

# 优先级  () > not > and > or

print(2 > 1 and 1 < 4 or 2 < 3 and 9 > 6 or 2 < 4 and 3 < 2)

# 先算and, 然后算or
# True

print(3 > 4 or 4 < 3 and 1 == 1)
# False
print(1 < 2 and 3 < 4 or 1 > 2)
# True
print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)
# True
print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)
# False
print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# False


print(1 or 2)
# 1
print(3 or 2)
# 3
print(0 or 2)
# 2
print(0 or 100)
# 100


# x or y  x为非零，返回x, x and y ,x如果为真，返回y
print(1 and 2)
print(0 and 2)

print(0 or 4 and 3 or 2)
# 3

print(2 or 1 < 3)
# 2
print(2 or 1 < 3 and 2)
# 2
print( 1 > 2 and 3 or 4 and 3 < 2)
# False