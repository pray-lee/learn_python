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
