from django.contrib.auth.models import User
from django.db import models
from .tasks import new_blog_body_text

import logging

logger = logging.getLogger(__name__)

def models_logger():
    return logger.debug("# ==== Calling: Models Logger ==== #")


class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=DRAFT)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Force validation on model save
        self.full_clean()
        super().save(*args, **kwargs)
        new_blog_body_text.delay(self.id)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def save(self, *args, **kwargs):
        # Force validation on model save
        self.full_clean()
        super().save(*args, **kwargs)
        models_logger()
