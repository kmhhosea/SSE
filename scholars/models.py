from django.db import models
return f"Profile({self.user.username})"


# Resource: a shared file or link (papers, code zip, book links)
class Resource(models.Model):
title = models.CharField(max_length=250)
description = models.TextField(blank=True)
link = models.URLField(blank=True)
file = models.FileField(upload_to='resources/', blank=True, null=True)
uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
return self.title


# Post: for discussion feed similar to Reddit posts
class Post(models.Model):
author = models.ForeignKey(User, on_delete=models.CASCADE)
title = models.CharField(max_length=250)
body = models.TextField()
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
# simple counters
upvotes = models.IntegerField(default=0)
downvotes = models.IntegerField(default=0)
# optional: tag to classify the post (e.g., 'ai', 'applications', 'life')
tag = models.CharField(max_length=80, blank=True)


def __str__(self):
return f"Post({self.title}) by {self.author.username}"


# Comment: threaded comments (one-level reply)
class Comment(models.Model):
post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
author = models.ForeignKey(User, on_delete=models.CASCADE)
parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
body = models.TextField()
created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
return f"Comment by {self.author.username} on {self.post.title}"


# Notification: simple notification model to store messages
class Notification(models.Model):
user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
message = models.CharField(max_length=300)
is_read = models.BooleanField(default=False)
created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
return f"Notif({self.user.username}): {self.message[:30]}"