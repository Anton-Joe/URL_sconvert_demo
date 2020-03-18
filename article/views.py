from django.http import HttpResponse


def index(request):
    return HttpResponse('首页')


def article_list(request, categories):
    text = "您填写的分类是 %s" % categories
    return HttpResponse(text)