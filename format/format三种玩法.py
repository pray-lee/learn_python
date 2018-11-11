# s = '我叫{}, 今年{}, 爱好{}'.format('太保', 36, 'girl')
# print(s)
# s1 = '我叫{0}, 今年{1}, 爱好{2}, 再说一下我叫{0}'.format('太保', 36, 'girl')
# print(s1)
# s2 = '我叫{name}, 今年{age}, 爱好{hobbie}, 再说意思我叫{name}'.format(age=36, hobbie='girl', name='太保')
# print(s2)



str = '擦擦擦{}, 嘎嘎嘎{}, gegege{}'.format('1', '2', '3')
print(str)
str1 = '擦擦擦{0}, 嘎嘎嘎{2}, gegege{1}, cacaca{0}'.format('1', '2', '3')
print(str1)
str2 = '擦擦擦{first}, 嘎嘎嘎{second}, gegege{third}, cacaca{fouth}'.format(first="-first", second="-second", third="-third", fouth="-fouth")
print(str2)