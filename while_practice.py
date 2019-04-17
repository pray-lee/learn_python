#while
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 让用户选择何时退出
prompt = '\nTell me something, and i will repeat it back to you:'
prompt += '\n Enter "quit" to end the program. '
message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)




# 三次登陆
#
# i = 0
# while i < 3:
    # username = input('请输入用户名')
    # password = int(input('请输入密码'))
    # if username == 'lee' and password == 123:
        # print('登陆成功')
        # break
    # else:
        # print('请重新登陆')
    # i += 1


