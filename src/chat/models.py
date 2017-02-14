from __future__ import unicode_literals

from django.db import models

# Create your models here.
import core
from core.models import Authored, Active, Dated


class Chat(Authored, Dated, Active):
    chat_name = models.CharField(max_length=255, verbose_name='Chat name')
    members = models.ManyToManyField(core.models.User, related_name='chats')

