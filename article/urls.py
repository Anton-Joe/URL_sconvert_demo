from django.urls import re_path, path, converters, register_converter
from . import views


urlpatterns = [
    # \w 0-9 , a-z ,A-z , _
    # re_path(r'list/(?P<categories>\w+|(\w+\+\w+)+)/' ,views.article_list),
    path('', views.index),
    path('list/<cate:categories>', views.article_list, name='list')
]