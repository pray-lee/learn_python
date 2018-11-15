# send
def generator():
    print(1)
    result = yield 1
    print(1, result)
    result1 = yield 2
    print(2, result1)
    result2 = yield 3
    print(3, result2)
    yield


g = generator()
g.__next__()
g.send('send') #效果和next方法类似
g.send('send1')
g.send('send2')
# send方法想要使用，第一次调用生成器必须使用next方法, 生成器里最后一个yield不能接收外部的值

# 再写一次
def generator1():
    print(0)
    num1 = yield 1
    print(num1)
    num2 = yield(2)
    print(num2)
    yield

g1 = generator1()
g1.__next__()
g1.send('num1')
g1.send('num2')



# ******************************************************************************************


# 给移动平均值的average函数加一个init装饰器,让其自动执行next方法,以后就可以直接调用send方法获取平均值了
def init(f):
    def inner(*args, **kw):
        g = f(*args, **kw)
        g.__next__()
        return g
    return inner



# 获取移动平均值
@init
def average():
    count = 0
    sum = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum/count

avg = average()
# avg.__next__()
print(avg.send(10))
print(avg.send(20))




# python3 关于生成器的新特性
def ge():
    a = '12345678'
    b = 'abcdefg'
    yield from a
    yield from b
gg = ge()
for i in gg:
    print(i)
