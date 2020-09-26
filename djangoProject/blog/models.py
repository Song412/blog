#!/usr/bin/env python
#-*- coding:UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class User(models.Model):
    name = models.CharField('名字',max_length=16)
    number = models.CharField('账号',max_length=11)
    password = models.CharField('密码',max_length=16)
    def __unicode__(self):
        return self.number

class Blog(models.Model):
    """
    博客
    """
    title = models.CharField('标题', max_length=32)
    content = models.TextField('博客正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    def __unicode__(self):
        return self.title


class Comment(models.Model):
    """
    评论
    """
    blog = models.ForeignKey(Blog, verbose_name='博客',on_delete=models.CASCADE)
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=240)
    created = models.DateTimeField('发布时间', auto_now_add=True)

    def __unicode__(self):
        return self.content