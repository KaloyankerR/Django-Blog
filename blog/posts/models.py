from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=55)
    body = models.CharField(max_length=1_000_000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
