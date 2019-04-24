"""定义learning_logs的URL模式"""
from django.urls import re_path

from . import views

# 如果在learning_log
# 下的urls.py里面增加了子路由，并且增加了命名空间，这里要再声明一下app_name才不会出现namespace
# is not registed的错误
app_name = '[learning_logs]'

urlpatterns = [
    # 主页
    re_path(r'^$', views.index, name='index'),
    # 主题
    re_path(r'^topics/$', views.topics, name='topics'),
    # 主题详情
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
]
