# 枚举  特点： 枚举里面的值是不可以修改的, 这是他最大的优点
from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 1
    BLACK = 3
    RED = 4

print(VIP.YELLOW)  # VIP.YELLOW 打印出的是枚举类型 <enum 'VIP'>
print(VIP.GREEN)
print(VIP.BLACK)
print(VIP.RED)

# 枚举获取数值
print(VIP.YELLOW.value) # 1

# 枚举获取标签的名字
print(VIP.YELLOW.name) # YELLOW

# 枚举类型
print(type(VIP['YELLOW'])) # <enum 'VIP'>

# 枚举遍历

for v in VIP:
    print(v) # VIP.YELLOW .... 如果name一样的话，只会输出一个，如果想输出两个: for v in VIP.__members__

# 枚举内部只能做等值比较和is操作符
print(VIP.YELLOW == VIP.GREEN) # True  GREEN是YELLOW的别名, 相当于YELLOW_ALIAS
print(VIP.YELLOW is VIP.YELLOW) # True