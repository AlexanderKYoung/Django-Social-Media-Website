from django.contrib import admin

# Register your models here.
from .models import Notification, Post, Reply, Activities, Shopping, Meeting, File, Health, Attendees
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Notification)
admin.site.register(Activities)
admin.site.register(Shopping)
admin.site.register(Meeting)
admin.site.register(Health)
admin.site.register(Attendees)
admin.site.register(File)