from django.urls import path
from project.views import index

urlpatterns = [
    # path（路由，视图函数名）
    path('index/', index),
]