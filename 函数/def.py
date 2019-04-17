# 函数
def greet_user():
    '''简单的问候语'''
    print('hello python')
greet_user()

def greet(msg):
    print(msg)
greet('hello python')

# 位置实参
def describe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + '"s name is' + pet_name.title() + '.')
describe_pet('hamster', 'harry')

# 关键字实参
def describe_pet1(animal_type, pet_name):
    '''显示宠物信息'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + '"s name is' + pet_name.title() + '.')
describe_pet1(animal_type='hamster', pet_name='harry')

# 默认值 这里注意形参的顺序，先是位置形参，然后是默认形参)
def describe_pet2(animal_type, pet_name='john'):
    '''显示宠物信息'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + '"s name is' + pet_name.title() + '.')
describe_pet2('hamster')


# 传递列表
def greet_users(names):
    for name in names:
        print(name)
greet_users(['lee', 'zhang'])

# 在函数中修改列表
list = [1, 2, 3]
def changeList(list):
    if list:
        list.pop()
    return list
while list:
    print(list)
    print('del is not completed')
    changeList(list)

# 传递任意数量的实参
def anything(*item):
    print(item)
anything(1)
anything(1, 24)

def anything1(name, *item):
    print(name)
    print(item)
anything1('lee', '1', 'zhang')


# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    '''创建一个字典,其中包含我们知道的有关用户的一切'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                             location="princeton")
print(user_profile)
