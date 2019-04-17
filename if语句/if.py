cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 比较数字
age = 18
print(age == 18)
print(age != 18)

# 检查多个条件
# and
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # False
age_1 = 22
print(age_0 >= 21 and age_1 >= 21) # True

# or
age_2 = 22
age_3 = 18
print(age_2 >= 21 or age_3 >= 21) # True
age_2 = 18
print(age_2 >= 21 or age_3 >= 21) #False

# 检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print( 'mushrooms' in requested_toppings) # True
print( 'pepperoni' in requested_toppings) # False

# 检查特定制是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
users = 'marie'
print(users not in banned_users) # true

# 如果是空列表，返回False
if []:
    print('list is empty')
else:
    print('list is not empty') # 输出这行

# 使用多个列表

