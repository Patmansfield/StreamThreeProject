from django.test import TestCase
from .models import Post
from django.core.urlresolvers import resolve


class PostTests (TestCase):

    def test_str(self):
        test_title = Post(title='Blog title test')
        self.assertEqual(str(test_title), 'Blog title test')

    def test_post_list_resolves(self):
        resolver = resolve('/blog/')
        self.assertEqual(resolver.view_name, 'post_list')
