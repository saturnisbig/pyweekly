from django.shortcuts import render
from django.views.generic.dates import (ArchiveIndexView, DateDetailView,
                                        YearArchiveView, MonthArchiveView,
                                        DayArchiveView)

from .models import Entry, Category


class EntryArchiveIndexView(ArchiveIndexView):
    model = Entry
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
