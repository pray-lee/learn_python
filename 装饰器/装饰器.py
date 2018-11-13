import time
# 定义一个装饰器 装饰器作用，用于封装函数，拓展不同的功能
def getRunTime(f):
    def inner(*args, **kwargs):
        # startTime = time.time()

        result = f(*args, **kwargs)

        # endTime = time.time()
        # print(endTime-startTime)
        return result
    return inner

def func():
    time.sleep(0.01)
    print(1)

# func = getRunTime(func)
# func ()



# 装饰器语法糖
@getRunTime         # 把func1函数放在装饰器里执行 格式: @装饰器函数名
def func1():        # 被装饰函数
    time.sleep(0.01)
    return '1111111'
result = func1()
print(result)



# 装饰器默写练习

def wrapper(f):
    def inner(*args,**kwargs):
        result = f(*args, **kwargs)
        return result
    return inner
@wrapper
def func2(b, a):
    print(1,b, a)
    return 'im func2'
result = func2(1111111, a = 1)
print(result)
