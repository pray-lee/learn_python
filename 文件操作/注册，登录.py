# username = input('请输入你的用户名')
# password = input('请输入你的密码')
# with open('list_of_info', mode="w", encoding="utf-8") as f:
#   f.write('{}\n{}'.format(username, password))

i = 0
lis = []
while i < 3:
  username = input('用户名')
  password = input('密码')
  with open('list_of_info', mode="r+", encoding="utf-8") as f1:
    for line in f1:
      lis.append(line)
  print(lis)    
  if username == lis[0].strip() and password == lis[1].strip():
    print('登录成功')
  else:
    print('账号和密码错误')
  i+=1