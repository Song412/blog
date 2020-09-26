#!/usr/bin/env python
#-*- coding:UTF-8 -*-
"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from blog.views import *
from django.conf.urls import url
from blog.models import *
admin.site.register([Blog])

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^/',login),

    url(r'^createee/(\d+)$', blog_create, name='blog_get_blog'),
    url(r'^createdaa/(\d+)$', creat_blog, name='create_blog'),
    url(r'^detailvs/$',registerHandler,name='blog_get_registerHandler'),
    url(r'^detailvd/$',loginl,name='blog_get_detailv'),
    url(r'^detailv/$',registerl,name='blog_get_register'),
    url('^detail/(\d+)/$',get_details ,name='blog_get_detail'),
]
