from django.shortcuts import render


def posts(request):
    render('blog/posts.html')


def post(request, slug):
    render('blog/post.html')
