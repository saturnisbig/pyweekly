from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from issues.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyweekly.views.home', name='home'),
    url(r'^issues/$', issues_list, name='issues'),
    url(r'^issues/(\d+)/', issue_articles_list),
    #url(r'^blog/', include('coltrane.urls')),
    url(r'^weblog/', include('weblog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
