from django.urls import re_path, path, converters, register_converter
from . import views


class CategoryConverter(object):
    regex = r'\w+|(\w+\+\w+)+/'

    def to_python(self, value):
        result = value.split('+')
        return result

    def to_url(self, value):
        if isinstance(value, list):
            result = '+'.join(value)
            return result
        else:
            return RuntimeError('转换ULR，分类参数必须为列表')


register_converter(CategoryConverter, 'cate')


urlpatterns = [
    # \w 0-9 , a-z ,A-z , _
    # re_path(r'list/(?P<categories>\w+|(\w+\+\w+)+)/' ,views.article_list),
    path('', views.index),
    path('list/<cate:categories>', views.article_list, name='list')
]