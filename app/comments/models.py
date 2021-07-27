from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)

    class Meta:

        ordering = ('created', )

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    email = models.EmailField()
    text = models.TextField()
    created = models.DateField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return self.text
