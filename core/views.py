from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.urls import reverse

import core.models
import core.forms
import core.filters

from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView

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
    title = 'Посты'

    def get_filters(self) -> core.filters.Post:
        return core.filters.Post(self.request.GET)

    def get_context_data(self, **kwargs):
        c = super().get_context_data()
        # c['form'] = core.forms.PostSearch(self.request.GET or None)
        c['filters'] = self.get_filters()
        return c

    def get_queryset(self):
        return self.get_filters().qs
        # queryset = core.models.Post.objects.all()
        # name = self.request.GET.get('name')
        # if name:
        #     queryset = core.models.Post.objects.filter(Q(body__icontains=name) | Q(title__icontains=name))
        # return queryset


class PostDetail(TitleMixin, DetailView):
    queryset = core.models.Post.objects.all()

    def get_title(self):
        return str(self.get_object())


class PostUpdate(TitleMixin, UpdateView):
    queryset = core.models.Post.objects.all()
    form_class = core.forms.PostEdit

    def get_title(self) -> str:
        return 'Редактирование' + str(self.get_object())

    def get_success_url(self):
        return reverse('core:list_view')


class PostDelete(TitleMixin, DeleteView):
    queryset = core.models.Post.objects.all()

    def get_title(self):
        return 'Удаление ' + str(self.get_object())

    def get_success_url(self):
        return reverse('core:list_view')
