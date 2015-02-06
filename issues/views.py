from django.shortcuts import render
from django.http import HttpResponse

from .models import Issue, Article


def issues_list(request):
    issues = Issue.objects.all()
    return render(request, 'issue_list.html', {'issues': issues})


def issue_articles_list(request, issue_num):
    issue = Issue.objects.get(issue_num=issue_num)
    if issue:
        articles = issue.article_set.all()
    else:
        print 'issue not found'
        articles = []
    return render(request, 'issue_article_list.html',
                  {'articles': articles})
