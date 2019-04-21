# 存储数据 (json)
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as file_object:
    # dump: 转储的意思,理解为存储
    json.dump(numbers, file_object)

# How to read json file?
filename = './numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)
print(numbers)
print(type(numbers)) # <class list>


# 实例，如果用户名存在则读取名字，如果没有用户名就让用户输入用户名
filename = 'username.json'
try:
    with open(filename) as file_object:
        username = json.load(file_object)
except:
    username = input('input your name ,please!')
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        print('save successed')
else:
    print(username)


# 重构 (每个函数只执行一个功能)
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except:
        return None
    else:
        return username

def set_new_username():
    filename = 'username.json'
    username = input('input your name please')
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print('*********')
        print(username)
        print('*********')
    else:
        username = set_new_username()
        print(username)
greet_user()
