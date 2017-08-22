from __future__ import unicode_literals
import re
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.

class UserManager(models.Manager):
    def isEntered(self, field, min):
        if len(field) < min:
            return False
        else:
            return True

    def isName(self, field):
        return NAME_REGEX.match(field)
    def isEmail(self, field):
        return EMAIL_REGEX.match(field)
    def getUsers(self):
        userlist = User.objects.all().order_by('goldtotal')
        return userlist

class User(models.Model):
    name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
