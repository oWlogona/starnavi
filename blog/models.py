from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    like_count = models.IntegerField(default=0)
    text = models.TextField()
    created_by = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, blank=True, on_delete=models.CASCADE)
