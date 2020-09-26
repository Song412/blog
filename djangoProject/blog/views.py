#!/usr/bin/env python
#-*- coding:UTF-8 -*-
from django.shortcuts import render
from django.template import RequestContext
# Create your views here.
from blog.models import *
from django.http import Http404
from .forms import CommentForm
from .forms import LoginForm
from .forms import RegisterForm
def get_blogs(request,u):
    blogs = u.blog.all()
    return render(request,'blog_list.html', {'blogs': blogs,'user':u.name})


def loginl(request):
    print(123456)
    form = LoginForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        print(cleaned_data)
        u = User.objects.get(number=cleaned_data['number'])
        if u.password == cleaned_data['password']:
            blogs = u.blog_set.all()
            return render(request, 'blog_list.html', {'blogs': blogs, 'user': u})
def login(request):
    form = LoginForm(request.POST)
    print(1234555)
    return render(request, 'login.html',{'form':form})

def get_details(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            print(cleaned_data)
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog_details.html', ctx)
#跳转注册界面
def registerl(request):
    form = RegisterForm(request.POST)
    return render(request, 'registered.html',{'form':form})

#注册
def registerHandler(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        u = User.objects.filter(number=cleaned_data['number'])
        if u.exists():
            form = RegisterForm(request.POST)
            return render(request, 'registered.html', {'form': form, 'errorMessage': "账号已存在"})
        User.objects.create(**cleaned_data)
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'message': "账号创建成功",'form': form,})

def creat_blog(request,user_id):
    return render(request, 'blog_create.html',{'user_id':user_id})
def blog_create(request,u_id):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get('content')
        u = User.objects.get(id=u_id)
        s ={'title':title,'content':content,'user':u}
        Blog.objects.create(**s)
        blogs = u.blog_set.all()
        return render(request, 'blog_list.html', {'blogs': blogs, 'user': u})

