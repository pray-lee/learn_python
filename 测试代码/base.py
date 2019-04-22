# 测试函数
def get_formatted_name(first, last):
    '''Generate a neatly formatted full name'''
    full_name = first + ' ' + last
    return full_name.title()

def get_formatted_name1(first, middle, last):
    '''生成整洁的姓名'''
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()

# 单元测试和测试用例， 一个测试用例可能包含多个单元测试

# 测试用例例子：
import unittest
'''*****这个类里面定义的test开头的方法都会被执行*****'''
class NamesTestCase(unittest.TestCase):
    '''测试get_formatted_name函数'''

    # 能通过的测试
    def test_first_last_name(self):
        '''能够正确的处理像janis joplin这样的姓名吗？'''
        formatted_name = get_formatted_name('janis','joplin') #执行函数
        self.assertEqual(formatted_name, 'Janis Joplin') #断言
        # (两个参数，一个是运行函数得到的结果，一个是期望的结果)

    # 不能通过的测试
    def test_first_middle_last(self):
        formatted_name = get_formatted_name1('lee','xiaoyong')
        self.assertEqual(formatted_name, 'lee xiaoyong')
unittest.main() # *****这句话意思是让python运行这个文件中的测试方法*****



