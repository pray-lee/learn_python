import re # 引入正则表达式

a = 'c|javascript|python'

print(re.findall('javascript', a)) # 得到一个列表 ['javascript']

b = 'c0a1b3c4v6b9&%'

print(re.findall('\d',b))
print(re.findall('[0-9]', b))

print(re.findall('\D', b))
print(re.findall('[^(0-9)]', b))

print(re.findall('\w', b))
print(re.findall('[A-Za-z0-9]', b))

print(re.findall('\W', b)) # 非单词字符 包括转义字符

print(re.findall('\s', b)) # 空白字符

print(re.findall('\S', b)) # 非空白字符


# 数量词

str = 'python 111javascript789php'

print(re.findall('[a-z]+', str)) # python javascript php


# 模式匹配   re.I 忽略大小写   re.S 匹配所有的字符,包括\n

# re 模块其他功能

language = 'pythonpythonjavascriptphp'

print(re.sub('python', 'go', language))  # 查找替换, 被替换，要替换，原始字符串

# sub第二个参数可以传函数
def convert(value):
    return value.group() + 'value.group'

print(re.sub('python', convert, language))




# group 使用 group(0)返回的是所有的结果，第一个结果以1开头
s = 'life is short, i use python'

r = re.search('(life)(.)*(python)', s)
print(r.group(1))