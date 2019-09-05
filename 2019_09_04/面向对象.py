# class
class Student():
    # 类变量
    name = 'hahaha'
    def __init__(self):
        #实例变量
        self.name = 'hehehe' 
        print(self.__class__.name) # hahaha 在实例方法里想使用类变量，可以使用self.__class__.varible 

    # 定义类方法,需要增加一个装饰器 classmethod   传入class参数
    @classmethod
    def plus_sum(cls):
        return cls.name, 'classmethod'

     #定义静态方法，需要增加一个装饰器 staticmethod   ,不需要传入参数  一般可以使用类方法代替, 尽量少用
    @staticmethod
    def add(x, y):
        return x + y, 'staticmethod'

print(Student().name) # hehehe
print(Student.name) # hahah  // 在外部调用类变量 ,直接使用class.varible
print(Student.plus_sum())
print(Student.add(1, 2))


# 成员的可见性 共有 私有 如果是私有的，在变量前面加双下划线,这样外面就不能访问了。
class Test():
    def __init__(self): 
        self.__score = 0 

    def __marketing(self, score):
        self.score = score

test = Test()
print(test.__dict__) # {_Test__score: 0}
print(test.__score) # 报错 , 提示没有__score变量
test.__marketing(56) # 报错 , 提示没有__marketing方法

# 继承