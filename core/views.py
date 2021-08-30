from django.shortcuts import render, get_object_or_404
from django.db.models import Q
import core.models
from django.views.generic import ListView

from .models import Post


# class BlogListView(ListView):
#    model = Post
#    template_name = 'home.html'


def list_view(request):

    posts = core.models.Post.objects.all()
    name = request.GET.get('name')
    if name:
        posts = core.models.Post.objects.filter(Q(body__icontains=name) | Q(title__icontains=name))
    return render(request, 'core/ListView.html', {'object_list': posts})


def index(request):
    posts = core.models.Post.objects.all()
    return render(request, 'core/index.html', {'object_list': posts})


def post_detail(request, pk):
    post = get_object_or_404(core.models.Post, pk=pk)
    return render(request, 'core/posts/detail.html', {'object': post})
