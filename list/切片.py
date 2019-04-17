# 切片 (还是返回列表)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])# charles martina michale
print(players[1:4])# martina michael florence

# 如果没有指定，默认从第一个读取
print(players[:4]) # charles martina michael florence

# 如果末尾没有指定，到结尾处结束
print(players[1:]) # martina michael florence eli

# 负数
print(players[-3:]) # michael florence eli

# 遍历
for player in players[:3]:
    print(player) # charles martina michael

# 复制列表
my_foods = ['pizza', 'falafel']
friends_foods = my_foods[:]
print(friends_foods)

# 动手试一试
print('The first three items in the list are:')
for i in players[:3]:
    print(i)
print('The last three items in the list are:')
for i in players[-3:]:
    print(i)

