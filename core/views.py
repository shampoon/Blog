from django.shortcuts import render, get_object_or_404
from django.db.models import Q
import core.models
from django.views.generic import ListView, TemplateView, DetailView

from .models import Post


class TitleMixin:
    title: str = None

    def get_title(self) -> str:
        return self.title

    def get_context_data(self, **kwargs):
        c = super().get_context_data()
        c['title'] = self.get_title()
        return c


class IndexView(TitleMixin, TemplateView):
    template_name = 'index.html'
    title = 'Глаавная'


class ListView(TitleMixin, ListView):
    #template_name = 'post_list.html'
    title = 'Посты'

    def get_queryset(self):
        queryset = core.models.Post.objects.all()
        name = self.request.GET.get('name')
        if name:
            queryset = core.models.Post.objects.filter(Q(body__icontains=name) | Q(title__icontains=name))
        return queryset


class PostDetail(TitleMixin, DetailView):
    queryset = core.models.Post.objects.all()

    def get_title(self):
        return str(self.get_object())
