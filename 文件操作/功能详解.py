f = open('./file.txt', mode="r+", encoding="utf-8")
#读三位英文字符
f.seek(3) #按照字节定光标的位置
# f.readline() # 一行一行读
# f.readlines() # 每一行当成列表中的一个元素，添加到list中
print(f.tell()) # 告诉你光标的位置

content = f.read(3)
print(content)
f.close()

# open的另外一种写法
with open('./file.txt', mode="r+", encoding="utf-8") as obj:
  print(obj.read())