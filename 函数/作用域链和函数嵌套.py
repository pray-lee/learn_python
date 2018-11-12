# nonlocal  # 声明了一个上层局部变量,只能用于局部变量
# global  # 声明了一个全局变量

# 闭包
def outer():
    a = 1
    def inner():
        print(a)
    print(inner.__closure__) # 判断是不是闭包

outer() # <cell at 0x10ef3ea08: int object at 0x10ecc6040> 如果打印的是cell开头的，说明这是闭包,如果打印的是None,则不是。




# 使用闭包的好处：只生成一次局部变量(url)，然后把获取url得到的数据封装成一个函数，返回出去，再多次调用的时候，就不用每次生成一个新的url，节省了内存空间

# 闭包应用
from urllib.request import urlopen
def getUrl(url):
    myurl = url
    def getFunc():
        result = urlopen(myurl).read()
        print(result)
    return getFunc
getUrlData = getUrl('http://www.baidu.com');
getUrlData()

#getUrlData()
#getUrlData()
#getUrlData()
#getUrlData()
#getUrlData()
#getUrlData()
#getUrlData()
#getUrlData()

# 个人重新封装一下,针对不同的链接，每个函数只执行一次可以使用这种方式,如果使用相同的链接，多次操作，使用上面的
#def getMyUrl(url): 
#    result = urlopen(url)
#    print(result)
