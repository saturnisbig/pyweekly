# -*- coding: utf-8 -*-

import datetime
from markdown import markdown

from django.db import models


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
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique_for_date="pub_date")
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    enable_comments = models.BooleanField(default=True)

    category = models.ForeignKey('Category')

    excerpt_html = models.TextField(editable=False)
    content_html = models.TextField(editable=False)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "entries/%s/" % self.slug
