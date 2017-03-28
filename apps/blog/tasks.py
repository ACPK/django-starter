from __future__ import absolute_import
from django.dispatch import receiver
from celery import shared_task

@shared_task
def new_blog_body_text(blog_id):
    from .models import Post
    get_post = Post.objects.get(pk=blog_id)
    if "Celery is good for you" not in get_post.body:
        get_post.body = get_post.body+"... Celery is good for you"
        Post.objects.filter(pk=blog_id).update(body=get_post.body)
        print("New text: %s" % (get_post.body))
    return 'Complete'