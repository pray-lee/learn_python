# 读取文件
with open('../log.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 逐行读取
filename = '../log.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

# 创建一个包含文件各行内容的列表
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)

