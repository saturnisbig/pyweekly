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
    DRAFT_STATUS = 1
    LIVE_STATUS = 2
    HIDE_STATUS = 3
    STATUS_CHOICES = (
        (DRAFT_STATUS, "草稿"),
        (LIVE_STATUS, "发布"),
        (HIDE_STATUS, "隐藏")
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique_for_date="pub_date")
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    status = models.SmallIntegerField(choices=STATUS_CHOICES,
                                      default=LIVE_STATUS)

    author = models.ForeignKey(User)
    categories = models.ManyToManyField(Category)

    excerpt_html = models.TextField(editable=False, blank=True)
    content_html = models.TextField(editable=False, blank=True)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "entries/%s/" % self.slug
