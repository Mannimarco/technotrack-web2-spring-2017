from __future__ import unicode_literals

from django.db import models

# Create your models here.
from core.models import Dated, User


class FriendshipRequest(Dated):
    from_user = models.ForeignKey(User, related_name='from_user_request', verbose_name='Request from')
    to_user = models.ForeignKey(User, related_name='to_user_request', verbose_name='Request to')
    is_accepted = models.BooleanField(default=False)


class Friends(Dated):
    user_1 = models.ForeignKey(User, related_name='user_1', verbose_name='user 2')
    user_2 = models.ForeignKey(User, related_name='user_2', verbose_name='user 1')

