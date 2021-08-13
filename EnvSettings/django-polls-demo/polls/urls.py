from django.conf.urls import url
from . import views
app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]  # 使用正则表达式匹配URL，并调用相应的视图
