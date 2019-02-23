# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class vehicle(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=25)
    description = models.TextField()
    color = models.CharField(max_length=20)
    doors = models.IntegerField(default=3)
    lot_number = models.IntegerField()
    def __str__(self):
        return self.model

# For Ldap
# class MyUser(AbstractUser):
#     from_ldap = models.BooleanField(
#         _('LDAP user'),
#         editable=False,
#         default=False
#     )
