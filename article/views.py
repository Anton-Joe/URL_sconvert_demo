from django.http import HttpResponse
from django.shortcuts import reverse


def index(request):
    return HttpResponse('首页')


def article_list(request, categories):
    # 函数传进来的categories，经过了处理：categories = CategoryConverter.to_python(categories)

    # reverse下的categories，经过了处理：categories = CategoryConverter.to_url(categories)
    path = reverse('list', kwargs={'categories': categories})
    print(path)

    text = "您填写的分类是 %s" % categories
    return HttpResponse(text)