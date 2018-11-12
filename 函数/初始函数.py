def mylen(s):
    i = 0
    for k in s:
        i += 1
    print(i)
    return i


mylen('safasdfasf')
length = mylen('123')
print(length)

# 参数定义
def func(a, b='2', c='3'):
    print(a, b, c)

func(1)

def func1(name, sex="男"):
    print('%s, %s' %(name, sex))
func1('李晓勇')
func1('苏文丽', '女')

# this is wrong ... 先定义位置参数，然后在定义默认参数**********************************************************
# def func2(sex="男", name):
#     print('%s, %s' %(name, sex))

# func2('女', '苏文丽')
# func2('男', name='李晓勇')

def func3(name, sex="男"):
    print('{}, {}'.format(name, sex))
func3(sex="女", name="苏文丽")
func3('李晓勇')

# 动态参数1  类似于js中的arguments, 适用于不确定有多少参数的情况 (只能接收位置传参)
def func4(*args):
    print(args) #type: tuple
func4(1,3,4,5)

# 动态参数2 （只可以接收默认参数）
def func5(**kwargs):
    print(kwargs) # type dict
func5(b=2, c=3)

# 混合参数  必须先args,然后kwargs, 因为形参必须先定义位置参数，再定义默认参数*******************************************
def func6(*args, **kwargs):
    print (args, kwargs)
func6(1,2,3,4,5,a=1,b=3)

def func7(a, *args, default='haha', **kwargs):
    print(a, args, default, kwargs)
func7(0, 3, 5, 6, default="hehe", aa=1, bb=2)
func7(0, 3, 5, 6, aa=1, bb=2)

#  总结，形参顺序： 位置参数->*args->默认参数->**kwargs****************************************************************

# 实参传参的方式 给一个序列加上*，就是将这个序列按照顺序打散，挨个传进去

def func8(*args):
    print(args)
list = [1,3,4,5,6,7]
func8(*list)

# 如果传递dict,则使用**
def func9(**kwargs):
    print(kwargs)
dict = {'a':1, 'b': 2}
func9(**dict)