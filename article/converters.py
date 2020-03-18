from django.urls import register_converter


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