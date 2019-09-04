# 转义字符  \
# 字符串前面加个r，说明是原始字符串,就不需要转义字符了
print(r'c:/window') # c:/window

# 字符串操作   重要
str = 'hello world'
# 可以用下标访问
print(str[0]) # 0

print(str[0:5]) # hello

print(str[0:-3]) # 删除最后三个字符 hello wo

print(str[6:])  #从第6个字符开始，截取到结束

print(str[-4:]) #从末尾倒数四个字符
