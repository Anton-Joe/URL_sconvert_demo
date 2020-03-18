from django.urls import re_path,path
from . import views
urlpatterns = [
    re_path(r'^[^+/].',views.article_list),
    path('', views.index)
]