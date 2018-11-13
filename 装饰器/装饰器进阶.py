# 装饰器进阶

# 复习
def wrapper(f):
    def inner(*args, **kwargs):
        print('被装饰的函数执行之前做的事')
        result =  f(*args, **kwargs)
        print('被装饰的函数执行之后做的事')
        return result,1 # 这个才是func1的真正返回值
    return inner

@wrapper
def func1(*args, **kwargs):
    print(args, kwargs)
    return 111 # 这个不是func1的返回值
result = func1(1, a=2)
