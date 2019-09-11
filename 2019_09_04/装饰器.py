# 装饰器
# 对修改是封闭的，对拓展是开放的

import time

# def f1():
    # print('This is a function')

# def print_current_time(func):
    # print(time.time())
    # func()

# print_current_time(f1)

# 装饰器实现

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper
def f2():
    print('This is a function 2')
