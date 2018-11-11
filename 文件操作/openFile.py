# 创建文件对象
f = open('./file.txt', mode="r", encoding="utf-8")
# 读取内容
content = f.read()
print(content)
# 关闭操作
f.close()
