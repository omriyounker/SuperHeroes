# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from ..login_app.models import User
# Create your models here.


class Power(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()


class Hero(models.Model):
    name = models.CharField(max_length=255)
    powers = models.ManyToManyField(Power, related_name = "heroes")
    liked = models.ManyToManyField(User, related_name = "likes")
