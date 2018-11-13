def test():
    print('娃哈哈')
# 查看字符串格式的函数名
print(test.__name__)


# python内置装饰器
from functools import wraps

def wrapper(f):
    @wraps(f) 
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
print(func1.__name__) # 不加python内置装饰器,打印inner, 加了内置装饰器，打印func1

# 带参数的装饰器

