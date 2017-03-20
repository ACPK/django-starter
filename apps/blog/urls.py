from django.conf.urls import url

from . import views


app_name = 'blog'
urlpatterns = [
    url(r'$', views.posts, name='posts'),
    url(r'/post/(?P<slug>[\w]+)$', views.post, name='post'),
]
