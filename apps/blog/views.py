from django.shortcuts import render

from .models import Post


def posts(request):
    posts = Post.objects.all().filter(status=Post.PUBLISHED)
    return render(request, 'blog/posts.html', {'posts': posts})


def post(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'blog/post.html', {'post': post})
