# 类基础

# 创建和使用
#### 创建类
class Dog():
    '''一次模拟小狗的简单尝试'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + 'is now sitting!')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')
#### 创建实例
my_dog = Dog('willie', 6)
print(my_dog.name.title() + '.')
print(str(my_dog.age) + ' years old.')
my_dog.sit()
my_dog.roll_over()

#### 使用类和实例
class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self, make, model, year):
        '''初始化汽车属性'''
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# 给属性指定默认值
class Car1():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 这里设置了默认值，形参里就不需要传入了

    def get_descriptive_name(self):
        pass

    def read_odometer(self):
        print(str(self.odometer_reading) + ' miles on it.')
my_new_car1 = Car1('audi', 'a4', '2016')
print(my_new_car1.read_odometer())

# 修改属性的值(修改的是实例的属性)
my_new_car1.odometer_reading = 23
my_new_car1.read_odometer() # 23
my_new_car11 = Car1('bmw', 'm3', 2018)
my_new_car11.read_odometer() # 0

# 通过方法修改属性的值
class Car2():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 这里设置了默认值，形参里就不需要传入了

    def get_descriptive_name(self):
        pass

    def read_odometer(self):
        print(str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can not roll back an odometer!')
my_new_car2 = Car2('audi', 'a4', 2018)
print(my_new_car2.odometer_reading) # 0
my_new_car2.update_odometer(10)
print(my_new_car2.odometer_reading) # 10

# 通过方法对属性的值进行递增
class Car3():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 这里设置了默认值，形参里就不需要传入了

    def get_descriptive_name(self):
        pass

    def read_odometer(self):
        print(str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can not roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles
my_new_car3 = Car3(' fararri', '458', 2019)
my_new_car3.increment_odometer(100)
print(my_new_car3.odometer_reading) # 100
my_new_car3.increment_odometer(100)
print(my_new_car3.odometer_reading) # 200

