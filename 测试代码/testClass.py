# 测试类

# 各种断言方法
# python在unittest.TestCase类种提供了很多断言方法
# 常用的
# assertEqual(a, b)     核实a == b
# assertNotEqual(a, b)     核实a != b
# assertTrue(x)     核实x为True
# assertFalse(y)     核实y 为False
# assertIn(item, list)     核实item在list中
# assertNotIn(item, list)     核实item不在list中


# 一个要测试的类
class AnonymousSurvey:

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print('Survey results:')
        for response in self.responses:
            print('- ' + response)

# 调用这个类
question = 'What language did you first learn to speak?'
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

print('\n Thank you to everyone who participated in the survey!')
my_survey.show_results()

# 测试这个类
import unittest
# class TestAnonymousSurvey(unittest.TestCase):

    # # 这是测试一个答案的
    # def test_store_single_response(self):
        # question = 'What language did you learn to speak?'
        # my_survey = AnonymousSurvey(question)
        # my_survey.store_response('Chinese')

        # # **
        # self.assertIn('Chinese', my_survey.responses)

    # def test_store_three_response(self):
        # question = 'What language did you learn to speak?'
        # my_survey = AnonymousSurvey(question)
        # my_languages = ['chinese', 'english', 'korean']
        # for response in my_languages:
            # my_survey.store_response(response)
        # for response in my_languages:
            # self.assertIn(response, my_survey.responses)
# unittest.main()
# 上面的代码有些重复

# setUp()
class TestAnonymousSurvey1(unittest.TestCase):

    def setUp(self):
        '''创建一个调查对象和一组答案，供使用的测试方法使用'''
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['chinese', 'english', 'korean']

    def test_store_single_response(self):
        print('hahaha')
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
unittest.main()
