# dict
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color']) # green
print(alien_0['points'])# 5

# 使用字典 (增删改查)

# 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 0
print(alien_0)

# 删除键值对
del alien_0['points']
print(alien_0)

# 遍历字典
user_0 = {
    'username': 'lee',
    'first': 'su',
    'last': 'wang'
}
for key, value in user_0.items():
    print(key)
    print(value)

# 遍历key (返回list)
for key in user_0.keys():
    print(key)

# 如果不输keys,values, items, 默认是keys
for key in user_0:
    print(key)

# 按顺序遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages):
    print(name)

# 遍历字典种的所有值
for value in favorite_languages.values():
    print(value)
# 如果获取的值里有重复的，想要去除重复的话用set()转换一下
print('----')
for value in set(favorite_languages.values()):
    print(value)
