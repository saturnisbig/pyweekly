#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django import template
from django.db.models import get_model

from coltrane.models import Entry


class LatestEntriesNode(template.Node):
    def render(self, context):
        context['latest_entries'] = Entry.live.all()[:5]
        return ''


def do_latest_entries(parser, token):
    return LatestEntriesNode()


def do_latest_content(parser, token):
    bits = token.split_contents()
    if len(bits) != 5:
        raise template.TemplateSyntaxError("'get_latest_content' tag take\
                                           exactly four arguments")
    model_args = bits[1].split('.')
    if len(model_args) != 2:
        raise template.TemplateSyntaxError("'get_latest_content' must be an\
                                           'application_name'.'model_name'\
                                           string.")
    model = get_model(*model_args)
    if model == None:
        raise template.TemplateSyntaxError("'get_latest_content' got an\
                                           invalid model: %s" % bits[1])
    return LatestContentNode(model, bits[2], bits[4])


class LatestContentNode(template.Node):
    def __init__(self, model, num, varname):
        self.model = model
        self.num = int(num)
        self.varname = varname

    def render(self, context):
        if self.num == 0:
            context[self.varname] = self.model._default_manager.all()
        else:
            context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''

register = template.Library()
register.tag('get_latest_entries', do_latest_entries)
register.tag('get_latest_content', do_latest_content)
