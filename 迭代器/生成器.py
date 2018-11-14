# 生成器本质是迭代器

# 生成器函数 yield不能和return共用
# def generator():
#     print(1)
#     yield 'a'
# g = generator() # 执行之后得到一个生成器
# print(generator().__next__())   #和JS的一样
# print('__iter__' in dir(g))


# eg:
def tail(filename):
    f = open(filename,'r', encoding="utf-8")
    while True:
        line = f.readline()
        if line.strip():
            yield line.strip()

ge = tail('file')
for i in ge:
    if 'python' in i:
        print('******', i)
