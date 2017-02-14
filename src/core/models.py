# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    first_name = models.CharField(max_length=25, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=25, blank=False, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар')


class Authored(models.Model):
    author = models.ForeignKey(User)

    class Meta:
        abstract = True


class Dated(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Active(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
