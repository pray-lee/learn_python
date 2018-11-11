# 创建文件对象 mode="r" r:只读  rb:非文字文件(上传和下载使用)（图片等）
f = open('./file.txt', mode="r", encoding="utf-8")
# 读取内容
content = f.read()
print(content)
# 关闭操作
f.close()



# 以什么编码存储，就以什么编码方式打开

