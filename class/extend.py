# 继承
### 父类
class Car:
    '''一次模拟汽车的简单尝试'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print(self.odometer_reading)

    def update_odometer(self, miles):
        self.odometer_reading = miles

    def increment_odometer(self, miles):
        self.odometer_reading += miles

### 子类
class ElectricCar(Car):
    '''电动汽车独特之处'''
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

### 给子类定义属性和方法

class ElectricCar1(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print('battery' + self.battery_size  + '.')

my_tesla1 = ElectricCar1('tesla', 'model s', 2019)
print(my_tesla1.battery_size)

### 重写父类的方法
#### 就是把父类里不想要的方法在子类重新实现即可

