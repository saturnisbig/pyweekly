from django.conf.urls import patterns, url

from weblog.views import CategoryListView, category_detail


urlpatterns = patterns('',
    url(r'^$', CategoryListView.as_view(), name="weblog_category_list"),
    url(r'^(?P<slug>[-\w]+)/$', category_detail),
)
