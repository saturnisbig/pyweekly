
from django.conf.urls import patterns, url
from coltrane.views import *


urlpatterns = patterns('',
    url(r'^$', EntryArchiveIndexView.as_view(), name="coltrane_entry_archive"),
    url(r'^(?P<year>\d{4})/$', EntryYearArchiveView.as_view()),
    url(ur'^(?P<year>\d{4})/(?P<month>\w{3})/$',
        EntryMonthArchiveView.as_view(), name="coltrane_entry_archive_month"),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
        EntryDayArchiveView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        EntryDateDetailView.as_view(), name="coltrane_entry_detail"),
)
