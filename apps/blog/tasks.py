from __future__ import absolute_import
from django.dispatch import receiver
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def new_blog_body_text(blog_id):
    from .models import Post
    
    get_post = Post.objects.get(pk=blog_id)
    if "Celery is good for you" not in get_post.body:
        get_post.body = get_post.body+"... Celery is good for you"
        Post.objects.filter(pk=blog_id).update(body=get_post.body)
        logger.debug("\n=====>New Blog Body Text for id: %d \nwith ==> New text: %s" % (blog_id, get_post.body))
    return logger.info("task: new_blog_body_text complete ---^<@")