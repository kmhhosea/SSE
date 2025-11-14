from django.contrib import admin
from .models import Profile, Resource, Post, Comment, Notification


admin.site.register(Profile)
admin.site.register(Resource)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Notification)