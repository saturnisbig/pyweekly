
from django.conf.urls import patterns, url

from coltrane.views import (LinkDateDetailView, LinkDayArchiveView,
                            LinkMonthArchiveView, LinkYearArchiveView,
                            LinkArchiveIndexView)


urlpatterns = patterns('coltrane.views',
    url(r'^$', LinkArchiveIndexView.as_view(),
        name='coltrane_link_archive'),
    url(r'^(?P<year>\d{4})/$', LinkYearArchiveView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', LinkMonthArchiveView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
        LinkDayArchiveView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        LinkDateDetailView.as_view(), name='coltrane_link_detail'),
)
