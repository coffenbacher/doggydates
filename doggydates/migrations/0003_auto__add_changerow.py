# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ChangeRow'
        db.create_table(u'doggydates_changerow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'doggydates', ['ChangeRow'])


    def backwards(self, orm):
        # Deleting model 'ChangeRow'
        db.delete_table(u'doggydates_changerow')


    models = {
        u'doggydates.changerow': {
            'Meta': {'object_name': 'ChangeRow'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'customer': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'doggydates.customerrow': {
            'Meta': {'object_name': 'CustomerRow'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'customer': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'day': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'dog': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'home': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True'}),
            'walker': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['doggydates']