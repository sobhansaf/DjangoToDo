from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    time = models.TimeField()
