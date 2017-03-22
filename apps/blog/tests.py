from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Post, Comment


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester')

    def test_missing_required_fields_fails_validation(self):
        with self.assertRaises(ValidationError) as e:
            Post.objects.create()
            self.assertIn('author', e)
            self.assertIn('title', e)
            self.assertIn('body', e)

    def test_valid_post_passes_validation(self):
        title = "Valid Post"
        body = "A test post."
        post = Post.objects.create(author=self.user, title=title, body=body)
        self.assertEqual(self.user.id, post.author.id)
        self.assertEqual(post.title, title)
        self.assertEqual(post.body, body)
