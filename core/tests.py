from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from core import models

class PostModel(TestCase):

    def setUp(self):
        user = User.objects.create(username='foo')
        self.Post = models.Post.objects.create(title='Test Post', author=user, body='This is body of Test Post')

    def testStr(self):
        self.assertEqual(
            str(self.Post),
            self.Post.title,
            'Строковое представление объекта Post долно быть равно значению атрибута name'
        )


class PostSearchTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='Po')
        self.Post1 = models.Post.objects.create(title='Test Post 1', author=user, body='This is body of Test Post 1')
        self.Post2 = models.Post.objects.create(title='Test Post 2', author=user, body='This is body of Test Post 2')

    def testWithoutParams(self):
        response = self.client.get(reverse('core:posts'))
        self.assertEqual(200, response.status_code)
        self.assertSequenceEqual(
            list(response.context['object_list']),
            list(models.Post.objects.all()),
            'При поиске без параметров должны выводиться все посты',
        )

    def testSearchByBody(self):
        response = self.client.get(reverse('core:posts'), data={'body': 'This is body of Test Post 2'})
        self.assertEqual(1, response.context['object_list'].count())
        self.assertEqual(
            'Test Post 2',
            response.context['object_list'].first().title,
        )
