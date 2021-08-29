from django.shortcuts import render

import core.models


def PostsList(request):
    posts = core.models.Post.objects.all()
    return render(request, 'core/index.html', {'object_list': posts})


def PostDetail(request, pk):
    post = core.models.Post.objects.all().filter(id=pk)
    return render(request, 'core/index.html', {'object_list': post})
