# 标准库

# example ( 有序字典 )
from collections import OrderedDict

favorite_laguages = OrderedDict()

favorite_laguages['jen'] = 'python'
favorite_laguages['sarah'] = 'c'
favorite_laguages['edward'] = 'ruby'
favorite_laguages['phil'] = 'python'
for name, language in favorite_laguages.items():
    print(name.title() + ' "s favorite language is ' + language.title() + '.')
