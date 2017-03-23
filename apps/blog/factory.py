import random

from django.contrib.auth.models import User
from factory import DjangoModelFactory, Faker, lazy_attribute, SubFactory
import factory

from . models import Post, Comment


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker('user_name')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    author = SubFactory(AuthorFactory)
    title = Faker('sentence')
    body = Faker('paragraph')

    @lazy_attribute
    def status(self):
        return random.choice([x[0] for x in Post.STATUS_CHOICES])


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    author = SubFactory(AuthorFactory)
    post = SubFactory(PostFactory)
    body = Faker('paragraph')
