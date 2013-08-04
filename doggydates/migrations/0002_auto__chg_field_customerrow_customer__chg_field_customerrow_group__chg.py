# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CustomerRow.customer'
        db.alter_column(u'doggydates_customerrow', 'customer', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'CustomerRow.group'
        db.alter_column(u'doggydates_customerrow', 'group', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'CustomerRow.notes'
        db.alter_column(u'doggydates_customerrow', 'notes', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'CustomerRow.dog'
        db.alter_column(u'doggydates_customerrow', 'dog', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'CustomerRow.email'
        db.alter_column(u'doggydates_customerrow', 'email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'CustomerRow.cell'
        db.alter_column(u'doggydates_customerrow', 'cell', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'CustomerRow.address'
        db.alter_column(u'doggydates_customerrow', 'address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'CustomerRow.walker'
        db.alter_column(u'doggydates_customerrow', 'walker', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'CustomerRow.home'
        db.alter_column(u'doggydates_customerrow', 'home', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'CustomerRow.day'
        db.alter_column(u'doggydates_customerrow', 'day', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'CustomerRow.customer'
        raise RuntimeError("Cannot reverse this migration. 'CustomerRow.customer' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'CustomerRow.group'
        raise RuntimeError("Cannot reverse this migration. 'CustomerRow.group' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'CustomerRow.notes'
        raise RuntimeError("Cannot reverse this migration. 'CustomerRow.notes' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'CustomerRow.dog'
        raise RuntimeError("Cannot reverse this migration. 'CustomerRow.dog' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'CustomerRow.email'
        raise RuntimeError("Cannot reverse this migration. 'CustomerRow.email' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'CustomerRow.cell'
        raise RuntimeError("Cannot reverse this migration. 'CustomerRow.cell' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'CustomerRow.address'
        raise RuntimeError("Cannot reverse this migration. 'CustomerRow.address' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'CustomerRow.walker'
        raise RuntimeError("Cannot reverse this migration. 'CustomerRow.walker' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'CustomerRow.home'
        raise RuntimeError("Cannot reverse this migration. 'CustomerRow.home' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'CustomerRow.day'
        raise RuntimeError("Cannot reverse this migration. 'CustomerRow.day' and its values cannot be restored.")

    models = {
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