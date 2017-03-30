import random

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from django.urls import reverse
from django.test.utils import override_settings

from .factory import AuthorFactory, PostFactory, CommentFactory
from .models import Post, Comment
from .tasks import new_blog_body_text


class PostTestCase(TestCase):
    def test_missing_required_fields_fails_validation(self):
        with self.assertRaises(ValidationError) as e:
            Post.objects.create()
            self.assertIn('author', e)
            self.assertIn('title', e)
            self.assertIn('body', e)

    def test_valid_post_passes_validation(self):
        post = PostFactory.create()
        self.assertIsNotNone(post.pk)

    def test_published_status_is_draft_by_default(self):
        post = Post()
        self.assertEqual(post.status, Post.DRAFT)


class CommentTestCase(TestCase):
    def test_missing_required_fields_fails_validation(self):
        with self.assertRaises(ValidationError) as e:
            Comment.objects.create()
            self.assertIn('author', e)
            self.assertIn('post', e)
            self.assertIn('body', e)

    def test_valid_comment_passes_validation(self):
        comment = CommentFactory.create()
        self.assertIsNotNone(comment.pk)


class RequestTestCase(TestCase):
    def test_posts_view_displays_published_post_titles(self):
        published_posts = PostFactory.create_batch(random.randint(1, 10), status=Post.PUBLISHED)
        draft_posts = PostFactory.create_batch(random.randint(1, 10), status=Post.DRAFT)

        c = Client()
        response = c.get(reverse('blog:posts'))

        self.assertTemplateUsed(response, 'blog/posts.html')

        for post in published_posts:
            self.assertContains(response, post.title, status_code=200)

        for post in draft_posts:
            self.assertNotContains(response, post.title, status_code=200)

    def test_post_view_displays_title_and_body(self):
        post = PostFactory.create(status=Post.PUBLISHED)

        c = Client()
        response = c.get(reverse('blog:post', kwargs={'id': post.id}))

        self.assertTemplateUsed(response, 'blog/post.html')
        self.assertContains(response, post.title)
        self.assertContains(response, post.body)
        

class CeleryWorkerTestCase(TestCase):
    @override_settings(CELERY_ALWAYS_EAGER=True, BROKER_BACKEND='memory')
    def test_new_blog_body_text(self):
        post = PostFactory.create()
        result = new_blog_body_text.delay(post.pk)
        self.assertTrue(result.successful())