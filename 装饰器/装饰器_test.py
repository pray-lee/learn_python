# 登录一次，以后一直可以使用一些函数功能
islogin = False
def login(f):
    def inner():
        global islogin
        if islogin:
            result = f()
            return result
        else:
            username = input('username:')
            password = input('password:')
            if username=="lixiaoyong" and password == "pray173":
                print('登陆成功')
                islogin = True
                result = f()
                return result
            else:
                print('登录失败')
                return 
    return inner


@login
def add():
    print('add')

@login
def remove():
    print('remove')

add()
remove()


# 编写装饰器，为多个函数加上记录调用功能
