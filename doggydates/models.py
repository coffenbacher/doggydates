from django.db import models

class CustomerRow(models.Model):
    customer = models.CharField(max_length = 200, null=True)
    day = models.CharField(max_length = 200, null=True)
    group = models.CharField(max_length = 200, null=True)
    walker = models.CharField(max_length = 200, null=True)
    address = models.CharField(max_length = 200, null=True)
    dog = models.CharField(max_length = 200, null=True)
    cell = models.CharField(max_length = 200, null=True)
    home = models.CharField(max_length = 200, null=True)
    email = models.CharField(max_length = 200, null=True)
    notes = models.TextField(max_length = 200, null=True)
    

class ChangeRow(models.Model):
    customer = models.CharField(max_length = 200, null=True)
    action = models.CharField(max_length = 200, null = True)
    date = models.DateField(null=True)
    group = models.CharField(max_length = 200, null = True)
