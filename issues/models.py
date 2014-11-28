# -*- coding: utf-8 -*-

import datetime

from django.db import models


class Category(models.Model):
    title = models.CharField(u'类别名称', max_length=200)
    description = models.TextField(u'类别简介', blank=True)
    ctime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title


class Issue(models.Model):
    issue_num = models.IntegerField(u'期数', help_text=u'必须是正整数')
    title = models.CharField(u'本期名称', max_length=200)
    description = models.TextField(u'关于本期的简介')
    ctime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Article(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDE_STATUS = 3
    STATUS_CHOICES = ((LIVE_STATUS, u'发布'),
                      (DRAFT_STATUS, u'草稿'),
                      (HIDE_STATUS, u'隐藏'),)
    title = models.CharField(u'标题', max_length=250)
    excerpt = models.TextField(u'内容介绍', blank=True)
    source_link = models.URLField(u'来源链接')
    translation_link = models.URLField(u'中文翻译链接', blank=True)
    pub_date = models.DateTimeField(u'发布时间', default=datetime.datetime.now)
    view_num = models.IntegerField(default=1)

    excerpt_html = models.TextField(editable=False, blank=True)

    issue = models.ManyToManyField(Issue)
    category = models.ForeignKey(Category)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS,
                                 help_text=u'只有文章为发布状态才会在页面显示')


    def __unicode__(self):
        return self.title
