from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from issues.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^issues/$', issues_list, name='issue_list'),
    url(r'^issues/(\d+)/', issue_articles_list),
    url(r'^weblog/', include('weblog.urls.entries')),
    url(r'^weblog/categories/', include('weblog.urls.categories')),

    url(r'^admin/', include(admin.site.urls)),
)
