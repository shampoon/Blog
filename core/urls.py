"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import core.views

app_name = 'core'

urlpatterns = [
    path('index', core.views.IndexView.as_view(), name='index'),
    path('list_view', core.views.ListView.as_view(), name='list_view'),
    path('post/<int:pk>', core.views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', core.views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', core.views.PostDelete.as_view(), name='post_delete'),
]
