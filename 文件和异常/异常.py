# 异常
# print(5/0) # python会报错

# 使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print('You cant divide by zero')

# else代码块:
# 依赖于try代码块成功执行的代码都应放到else代码块中
try:
    print(5/1)
except:
    print('you are wrong')
else:
    print('success')

# 处理FileNotFoundError异常
# filename = 'alice.txt'
# with open(filename) as file_object:
    # contents = file_object.read()
# 这个代码会报FileNotFoundError
# 用try except包起来
filename = 'alice.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except:
    print('file does not exist.')
else:
    print('file has been found.')

