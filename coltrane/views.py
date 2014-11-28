from django.shortcuts import render, get_object_or_404
from django.views.generic.dates import (ArchiveIndexView, YearArchiveView,
                                        MonthArchiveView, DayArchiveView,
                                        DateDetailView)
from django.views.generic.list import ListView
from django.utils import timezone

from coltrane.models import Entry, Link, Category
from taggit.models import Tag


class TagListView(ListView):
    model = Tag
    template_name = 'coltrane/tag_list.html'


def tag_entry_list(request, tagid):
    #t = str(tag)
    #t = Tag.objects.get(name__iexact=tag)
    t = get_object_or_404(Tag, id=tagid)
    return render(request, 'coltrane/tag_entry_list.html',
                  {'object_list': Entry.live.filter(tags=t)})


def tag_link_list(request, tag):
    pass


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def category_list(request):
    return render(request, 'coltrane/category_list.html', {
        'object_list': Category.objects.all()})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'coltrane/category_detail.html', {
        'object_list': category.live_entry_set()
    })


class EntryArchiveIndexView(ArchiveIndexView):
    queryset = Entry.live.all()
    date_field = "pub_date"
    make_object_list = True


class EntryYearArchiveView(YearArchiveView):
    queryset = Entry.live.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True


class EntryMonthArchiveView(MonthArchiveView):
    queryset = Entry.live.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True


class EntryDayArchiveView(DayArchiveView):
    queryset = Entry.live.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True


class EntryDateDetailView(DateDetailView):
    queryset = Entry.live.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True


class LinkArchiveIndexView(ArchiveIndexView):
    queryset = Link.objects.all()
    date_field = 'pub_date'


class LinkYearArchiveView(YearArchiveView):
    queryset = Link.objects.all()
    date_field = 'pub_date'
    make_object_list = True


class LinkMonthArchiveView(MonthArchiveView):
    queryset = Link.objects.all()
    date_field = 'pub_date'


class LinkDayArchiveView(DayArchiveView):
    queryset = Link.objects.all()
    date_field = 'pub_date'


class LinkDateDetailView(DateDetailView):
    queryset = Link.objects.all()
    date_field = 'pub_date'


def entries_index(request):
    return render(request, 'coltrane/entry_index.html',
                  {'entry_list': Entry.live.all()})


def entries_detail(request, year, month, day, slug):
    import datetime
    pub_date = datetime.datetime.strptime(year+month+day, '%Y%b%d')
    return render(request, 'coltrane/entry_detail.html',
                  {'entry': get_object_or_404(Entry,
                                              pub_date__year=pub_date.year,
                                              pub_date__month=pub_date.month,
                                              pub_date__day=pub_date.day,
                                              slug=slug)})
