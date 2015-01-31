# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Entry', fields ['slug']
        db.delete_unique(u'weblog_entry', ['slug'])

        # Adding field 'Entry.enable_comments'
        db.add_column(u'weblog_entry', 'enable_comments',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'Entry.pub_date'
        db.alter_column(u'weblog_entry', 'pub_date', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):
        # Deleting field 'Entry.enable_comments'
        db.delete_column(u'weblog_entry', 'enable_comments')

        # Adding unique constraint on 'Entry', fields ['slug']
        db.create_unique(u'weblog_entry', ['slug'])


        # Changing field 'Entry.pub_date'
        db.alter_column(u'weblog_entry', 'pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

    models = {
        u'weblog.category': {
            'Meta': {'ordering': "['title']", 'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'weblog.entry': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Entry'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['weblog.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_html': ('django.db.models.fields.TextField', [], {}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'excerpt_html': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['weblog']