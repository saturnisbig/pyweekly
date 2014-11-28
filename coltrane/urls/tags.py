#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from coltrane.views import TagListView, tag_entry_list, tag_link_list


urlpatterns = patterns('',
    url(r'^$', TagListView.as_view(), name="coltrane_tag_list"),
    url(r'^entries/(?P<tagid>\d+)/$', tag_entry_list,
        name="coltrane_tag_entry_list"),
    url(r'^links/(?P<tag>[-\w]+)/$', tag_link_list),
)
