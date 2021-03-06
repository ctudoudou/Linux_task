#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 下午4:51
# @Author  : tudoudou
# @File    : urls.py
# @Software: PyCharm

"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('rooms/', rooms, name='room'),
    path('news/', news,name='news'),
    path('article/',article,name='article'),
    path('email/',email,name='email'),
    path('gallery/',gallery,name='gallery'),
    path('user/',user,name='user'),
    path('yuding/',yuding,name='yuding'),
]
