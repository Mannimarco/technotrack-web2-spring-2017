from __future__ import unicode_literals

from django.db import models

# Create your models here.
from core.models import Authored, Dated, Active
from chat.models import Chat


class Message(Authored, Dated, Active):
    text = models.TextField()
    chat = models.ForeignKey(Chat, related_name='messages')
