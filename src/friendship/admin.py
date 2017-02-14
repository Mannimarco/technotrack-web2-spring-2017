from django.contrib import admin

# Register your models here.
from models import Friends, FriendshipRequest

admin.site.register(Friends)
admin.site.register(FriendshipRequest)
