from django.contrib import admin
from .models import UserTag, EventTag, Tag, User, Event
# Register your models here.

admin.site.register(UserTag)
admin.site.register(EventTag)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Event)