"""定义learning_logs的URL模式"""
from django.urls import re_path

from . import views

urlpatterns = [
    # 主页
    re_path(r'^$', views.index, name='index')
]
