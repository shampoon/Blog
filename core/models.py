from django.db import models
from django.db import models


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField('Блог')
    pub_date = models.DateField('Дата публикации')
    mod_date = models.DateField('Дата модификации')
    rating = models.IntegerField('Рейтинг')

    def __str__(self):
        return self.title
