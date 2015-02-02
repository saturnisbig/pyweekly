from django.conf.urls import patterns, url

from weblog.views import *

urlpatterns = patterns('',
    url(r'^$', EntryArchiveIndexView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        EntryDateDetailView.as_view(), name='entry_detail'),
    url(r'^(?P<year>\d{4})/$', EntryYearArchiveView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        EntryMonthArchiveView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        EntryDayArchiveView.as_view()),
)

urlpatterns += patterns('',
    url(r'^categories/$', CategoryListView.as_view()),
    url(r'^categories/(?P<slug>[-\w]+)/$', category_detail),
)
