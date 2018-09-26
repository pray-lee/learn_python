# 字符串的索引与切片
# 索引
# str = 'abcdefghijk'
# print(str[0])
# print(str[1])

# 切片
# print(str[0:3])
# print(str[0:])   # 默认到最后
# print(str[0:-1]) # 最后一个
# print(str[0:5:2]) # 加步长
# print(str[5:0:-2]) #反向加步长


# 字符串操作方法
# s = 'leexIAoyOng'
# print(s.capitalize())  #首字母变成大写
# print(s.upper())   # 全部变成大写
# print(s.lower())  # 全部变成小写
# print(s.swapcase()) #字符串中的大小写反过来（大写变小写，小写变大写）

# s = 'lee xiao yong '
# print(s.title())  #每个隔开(特殊字符或者数字)的首字母变大写
#
# s = 'lee^xiao&yong'
# print(s.title())
#
# s = 'alexWUsir'
# print(s.center(20, '-'))   # 文本居中，用的比较少
#
# s = 'ale\tUsir'
# print(s.expandtabs())  #不足八位的补成8位，大于八位的补成16位

# 公共方法
# s = 'leexiaoyong'
# print(len(s))
# s = 'leexiaoyong'
# print(s.startswith('l'))
# print(s.startswith('lee'))
# print(s.startswith('lex'))
# print(s.startswith('x', 3))  # 从第三位开始，以x开头
# print(s.startswith('x', 3, 5)) #在3，5区间内，是不是以x开头

# s = 'alexWUsir'
# print(s.find('s'))   # 寻找s对应的下标，找不到返回-1
# print(s.index('s'))  # 同上，找不到报错

# s = '  lee xiao yong '
# print(s.strip())   # 默认去除首尾空格
# s = '&lee$xiao@yong^'
# print(s.strip('&^'))  # 去除开头和结尾有$^特殊字符的
# s = '#leexiaoyong#'
# print(s.lstrip('#'))  # 删除左边的
# print(s.rstrip('#'))    # 删除右边的

# s = 'asdasdfasdfasdfasdfasdf'
# print(s.count('as')) # 寻找字符串里有多少个as

# s = 'lee-xiao=-yong'
# print(s.split('-'))  # 和js相同
#
# s = '中华人民共和国中华'
# print(s.replace('中华', '老王'))     # 默认全部替换
# print(s.replace('中华', '老王', 1))  # 只替换1次

# is系列
# str = 'leexiaoyong123'
# print(str.isalnum())  #字符串是否由字母或者数字组成
# print(str.isalpha())  #字符串是否只由字母组成
# print(str.isdigit())  #字符串是否只由数字组成

