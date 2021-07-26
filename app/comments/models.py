from django.db import models


class BlogPost(models.Model):

    title = models.CharField(max_length=150)
    body = models.TextField()
    comments = models.ForeignKey('Comments', on_delete=models.CASCADE, related_name='blog_post')


class Comments(models.Model):
    ...
