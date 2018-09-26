# 格式化输出
# % s d s:str   d: digital
name = input('请输入姓名')
age = input('请输入年龄')
height = input('请输入身高')
msg = '我叫%s, 今年%s, 身高%s， 学习进度5%%' % (name, age, height)
print(msg)

# example


# age = input('年龄')
# job = input('工作')
# hobbie = input('爱好')
# msg = '''
# ----------info of %s-----------
# Name: %s
# Age: %d
# Job: %s
# Hobbie: %s
# ----------end-----------
# ''' % (name, name, int(age), job, hobbie)
# print(msg)
