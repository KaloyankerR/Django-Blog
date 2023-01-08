from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=55)
    body = models.CharField(max_length=1_000_000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)