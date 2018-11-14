# 只有内置方法里面有__iter__方法的数据类型才可以被for循环

list = []
print(list.__iter__())

# 查看list的所有方法
# print(dir([]))

# 获取list1的迭代器
list1 = [1]
list1.__iter__() # 得到迭代器, 迭代器才有__next__方法
print(list1.__iter__().__next__()) # 获取list1的下一个, 和JS的迭代器类似

# 只要含有__iter__方法的都是可迭代的 --可迭代协议
# 内部含有__next__ 和__iter__方法的就是迭代器

# example
from collections.abc import Iterable
from collections.abc import Iterator
print(isinstance([], Iterable)) # True []是一个可迭代数据类型
print(isinstance([], Iterator)) # False []不是迭代器

# 迭代器的好处：
    # 遍历取值
    # 节省内存空间
        # 迭代器并不会在内存中在占用一大块内存，而是随着循环每次生成一个,不是一次性生成


# practice 模拟for循环

l = [1, 2, 3, 4]
iterator = l.__iter__()
while True:
    print(iterator.__next__())

