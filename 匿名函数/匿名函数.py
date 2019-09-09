# 普通函数声明
def add(a, b):
    return a + b

#匿名函数
add1 = lambda a, b: a+b
print(add(1, 2))
print(add1(1, 2))

# 匿名函数和max合用

dic = {
    "k1": 10,
    "k2": 100,
    "k3": 30
}

# 1
def func(key):
    return dic[key]
print(max(dic, key=func))
# 2
print(max(dic, key=lambda i: dic[i]))

# 函数里可以使用key的一共只有5个
# max, min, sorted, filter, map

# 面试题
d = lambda p:p*2
t = lambda p:p*3
x = 2
x = d(x)
x = t(x)
x = d(x)
print(x)

# 面试题1
# (('a'), ('b'))  (('c'), ('d')) 把这俩转成[{a:c}, {b:d}]
tuple1 = (('a'), ('b'))
tuple2 = (('c'), ('d'))
zip1 = zip(tuple1, tuple2) # (a,c) (b,d)
def func(tuple):
    return {tuple[0]: tuple[1]}
result = map(func, zip1)
print(list(result))

