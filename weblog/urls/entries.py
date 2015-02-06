from django.conf.urls import patterns, url

from weblog.views import (EntryDayArchiveView, EntryDateDetailView,
                          EntryYearArchiveView, EntryMonthArchiveView,
                          EntryArchiveIndexView)


urlpatterns = patterns('',
    url(r'^$', EntryArchiveIndexView.as_view(), name="weblog_entry_archive"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        EntryDateDetailView.as_view(), name='entry_detail'),
    url(r'^(?P<year>\d{4})/$', EntryYearArchiveView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        EntryMonthArchiveView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        EntryDayArchiveView.as_view()),
)
