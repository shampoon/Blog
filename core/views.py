from django.shortcuts import render

import core.models
from django.views.generic import ListView

from .models import Post


# class BlogListView(ListView):
#    model = Post
#    template_name = 'home.html'


def list_view(request):
    posts = core.models.Post.objects.all()
    return render(request, 'core/ListView.html', {'object_list': posts})


def index(request):
    posts = core.models.Post.objects.all()
    return render(request, 'core/index.html', {'object_list': posts})


def post_detail(request, pk):
    post = core.models.Post.objects.get(id=pk)
    return render(request, 'core/posts/detail.html', {'object': post})
