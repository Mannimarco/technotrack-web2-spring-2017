from __future__ import unicode_literals

from django.db import models

# Create your models here.
from core.models import Authored, Active, Dated


class Post(Authored, Dated, Active):
    text = models.TextField()
