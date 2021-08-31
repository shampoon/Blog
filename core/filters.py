import django_filters

from core import models


class Post(django_filters.FilterSet):
    body = django_filters.Filter(lookup_expr='icontains')
    class Meta:
        model = models.Post
        fields = ('body', )
