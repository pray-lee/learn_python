from django.db import models

# Create your models here.
# 模型告诉Django如何处理应用程序中存储的数据
# 在代码层面，模型就是一个类，包含属性和方法

# 下面是创建用户将要存储的主题的模型：


class Topic (models.Model):

    """用户学习的主题"""
    text = models.CharField(max_length=200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

# 我们需要告诉Django，默认应使用哪个属性来显示有关主题的信息。Django调用方法__str__()来显示模型的简单表示。在这里，我们编写了方法__str__()，它返回存储在属性text中的字符串

# 激活模型
# 要使用模型，必须让Django将应用程序包含到项目中。为此，打开settings.py（它位于目录learning_log/learning_log中），你将看到一个这样的片段，INSTALLED_APPS,把learning_logs加在这个列表中即可

