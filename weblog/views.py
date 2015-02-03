from django.shortcuts import render
from django.views.generic.dates import (ArchiveIndexView, DateDetailView,
                                        YearArchiveView, MonthArchiveView,
                                        DayArchiveView)
from django.views.generic.list import ListView

from .models import Entry, Category


class CategoryListView(ListView):
    model = Category
    context_object_name = "categories"


def category_detail(request, slug):
    cat = Category.objects.get(slug=slug)
    entries = cat.entries.all()
    return render(request, 'weblog/entry_archive.html', {'entries': entries})


class EntryArchiveIndexView(ArchiveIndexView):
    queryset = Entry.live.all()
    date_field = "pub_date"
    context_object_name = "entries"
    #template_name = 'weblog/entry_archive.html'


class EntryDateDetailView(DateDetailView):
    model = Entry
    context_object_name = "entry"
    date_field = "pub_date"
    month_format = "%m"   # default is %b


class EntryYearArchiveView(YearArchiveView):
    model = Entry
    make_object_list = True
    context_object_name = "entries"
    date_field = "pub_date"
    template_name = 'weblog/entry_archive.html'
    allow_future = True


class EntryMonthArchiveView(MonthArchiveView):
    model = Entry
    context_object_name = "entries"
    date_field = "pub_date"
    month_format = "%m"
    template_name = 'weblog/entry_archive.html'


class EntryDayArchiveView(DayArchiveView):
    model = Entry
    context_object_name = "entries"
    date_field = "pub_date"
    month_format = "%m"
    template_name = 'weblog/entry_archive.html'
