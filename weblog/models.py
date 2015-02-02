# -*- coding: utf-8 -*-

import datetime
from markdown import markdown

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


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
        return "/weblog/categories/%s/" % self.slug


class Entry(models.Model):
    DRAFT_STATUS = 1
    LIVE_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (DRAFT_STATUS, "草稿"),
        (LIVE_STATUS, "发布"),
        (HIDDEN_STATUS, "隐藏")
    )
    # Core fields.
    title = models.CharField(max_length=200)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    # Fields to store genereted HTML.
    excerpt_html = models.TextField(editable=False, blank=True)
    content_html = models.TextField(editable=False, blank=True)

    # Metadata.
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique_for_date="pub_date")
    status = models.SmallIntegerField(choices=STATUS_CHOICES,
                                      default=LIVE_STATUS)

    # Categories.
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.content_html = markdown(self.content)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        return like 'entries/2015/02/01/python-unittest/'
        """
        return reverse('entry_detail', args=[self.pub_date.strftime("%Y"),
                                             self.pub_date.strftime("%m"),
                                             self.pub_date.strftime("%d"),
                                             self.slug])
        #return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y/%m/%d"),
        #                           self.slug)
