# f = open('./log.txt', mode="w", encoding="utf-8")
# f.write('你笑iyonog')
# f.close()

# 追加
# ff = open('./log.txt', mode="a", encoding="utf-8")
# ff.write('++++')
# ff.close()
# 如果没有文件，就会创建文件,如果有，就会重写

# r+ 读写
#r+b 读写（以bytes类型读写）

# 最常用的就是r+ (可以边读边写)

fff = open('./log.txt', mode="r+", encoding="utf-8")
content1 = fff.read()
print(content1)
fff.write('hahaha')
fff.close()