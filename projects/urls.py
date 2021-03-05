"""
=================
Author:delpan
Time:2021/3/4,0004
=================
"""

from django.urls import path

from projects.views import index
from projects import views


#1、每一个应用（模块）都会维护一个子路由（当前应用的路由信息）
#2、跟主路由一样，也是从上到下匹配
#3、能够匹配上。则执行path第二个参数指定的视图，匹配不上抛404异常
urlpatterns = [
    #path('index/', index)
    #如果为类视图，path第二个参数为类视图名.as_view()
    path('',views.IndexView.as_view())
]