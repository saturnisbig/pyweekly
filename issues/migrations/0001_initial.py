# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Issue'
        db.create_table(u'issues_issue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue_num', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('ctime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'issues', ['Issue'])

        # Adding model 'Article'
        db.create_table(u'issues_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('excerpt', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('source_link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('translation_link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('view_num', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('excerpt_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'issues', ['Article'])

        # Adding M2M table for field issue on 'Article'
        m2m_table_name = db.shorten_name(u'issues_article_issue')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'issues.article'], null=False)),
            ('issue', models.ForeignKey(orm[u'issues.issue'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'issue_id'])


    def backwards(self, orm):
        # Deleting model 'Issue'
        db.delete_table(u'issues_issue')

        # Deleting model 'Article'
        db.delete_table(u'issues_article')

        # Removing M2M table for field issue on 'Article'
        db.delete_table(db.shorten_name(u'issues_article_issue'))


    models = {
        u'issues.article': {
            'Meta': {'object_name': 'Article'},
            'excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'excerpt_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['issues.Issue']", 'symmetrical': 'False'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'source_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'translation_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'view_num': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'issues.issue': {
            'Meta': {'object_name': 'Issue'},
            'ctime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_num': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['issues']