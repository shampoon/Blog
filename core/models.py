from django.db import models
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title
