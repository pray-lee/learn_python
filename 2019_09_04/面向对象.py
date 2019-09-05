# class
class Student():
    # 类变量
    name = 'hahaha'
    def __init__(self):
        #实例变量
        self.name = 'hehehe' 
        print(self.__class__.name) # hahaha 在实例方法里想使用类变量，可以使用self.__class__.varible 
print(Student().name) # hehehe
print(Student.name) # hahah  // 在外部调用类变量 ,直接使用class.varible