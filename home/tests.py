from __future__ import unicode_literals
from django.core.urlresolvers import resolve
from django.test import TestCase
from home.views import get_index
from home.views import articleone


class PageTest(TestCase):

    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

    def test_article_page(self):
        article_one = resolve('/articleone/')
        self.assertEqual(article_one.func, articleone)
