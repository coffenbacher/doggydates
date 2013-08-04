# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomerRow'
        db.create_table(u'doggydates_customerrow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('walker', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('dog', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cell', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('home', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=200)),
        ))
        db.send_create_signal(u'doggydates', ['CustomerRow'])


    def backwards(self, orm):
        # Deleting model 'CustomerRow'
        db.delete_table(u'doggydates_customerrow')


    models = {
        u'doggydates.customerrow': {
            'Meta': {'object_name': 'CustomerRow'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'customer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'day': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dog': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'home': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'walker': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['doggydates']