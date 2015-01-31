# -*- coding: utf-8 -*-

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
