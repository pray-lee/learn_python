# 包下面可以有多个模块，每个模块可以有多个类, 类里面有函数和变量

# import package/module   导入包/模块, 这个不能直接导入变量，只能先导入包/模块，然后package.module.xxx访问
# from package import module   导入模块
# from package.module/module import varible   导入模块里面的变量
# from package.module/module import *   导入模块内的所有变量，可以直接使用, 不建议
# from package.module/module import a, b, c  导入module里面的a,b,c变量

# __init__.py文件的作用:
    # 在导入包或者包下面的模块的时候，这个文件会被python解释器自动执行, 一般里面放一些模块导入语句，在别的地方引用这个包的时候，会自动执行__init__，这样就不用在别的文件里面都分别导入这些模块了

# 包和模块不会被重复导入, 即使写多次，也只会导入第一次

# 避免循环引用

# python如果导入了一个模块，则会自动执行这个模块里面的代码
