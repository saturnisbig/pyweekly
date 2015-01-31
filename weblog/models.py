# -*- coding: utf-8 -*-

import datetime
from markdown import markdown

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(u'类别标题', max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug


class Entry(models.Model):
    DRAFT = 1
    LIVE = 2
    HIDE = 3
    STATUS_CHOICES = (
        (DRAFT, "草稿"),
        (LIVE, "发布"),
        (HIDE, "隐藏")
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique_for_date="pub_date")
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    enable_comments = models.BooleanField(default=True)

    author = models.ForeignKey(User)
    categories = models.ManyToManyField(Category)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=LIVE)

    excerpt_html = models.TextField(editable=False)
    content_html = models.TextField(editable=False)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "entries/%s/" % self.slug
