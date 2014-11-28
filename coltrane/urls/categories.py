#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('coltrane.views',
    url(r'^$', 'category_list', name="coltrane_category_list"),
    url(r'^(?P<slug>[-\w]+)/$', 'category_detail',
        name='coltrane_category_detail'),
)
