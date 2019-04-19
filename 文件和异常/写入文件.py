# 写入文件
filename = './programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming")

# 写入多行
with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.')

# 追加内容到文件
with open(filename, 'a') as file_object:
    file_object.write('\nappend contents')

# r+

