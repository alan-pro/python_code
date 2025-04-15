from django.urls import path
from project02.views import index


urlpatterns = [
    path('index/', index),
]
