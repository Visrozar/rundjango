from __future__ import unicode_literals

from django.db import models

class Company(models.Model):
    title = models.CharField(max_length=200)
    company_id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.title