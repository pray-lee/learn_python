# count = 0
# while count < 10:
#     count += 1
#     if count == 7:
#         continue
#     print(count)
#
# count = 0
# while count < 10:
#     count += 1
#     if count == 7:
#         pass
#     else:
#         print(count)

# 1-100的奇数
# count = 1
#  方法1
#  while count < 101:
#      print(count)
#      count += 2
#  方法2
# count = 1
# while count < 101:
#     count += 2
#     if count % 2 == 1:
#         print(count)

# 求 1-2 + 3 -4 。。。的和
# sum = 0
# count = 1
# while count < 100:
#     if count % 2 == 0:
#         sum = sum - count
#     else:
#         sum = sum + count
#     count += 1
# print(sum)

# 三次登陆
#
i = 0
while i < 3:
    username = input('请输入用户名')
    password = int(input('请输入密码'))
    if username == 'lee' and password == 123:
        print('登陆成功')
        break
    else:
        print('请重新登陆')
    i += 1


