# 闭包 closure
# 一切皆对象
# 函数嵌套
def curve_pre():
    a = 1
    def curve():
        print('curve')
        print(a)
    return curve

f = curve_pre()
f()
