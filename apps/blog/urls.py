from django.conf.urls import url

from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^post/(?P<id>[0-9]+)/$', views.post, name='post'),
]
