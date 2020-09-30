from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class tweets(models.Model):
    text = models.TextField(max_length=300,default='')
    datetime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User,on_delete=models.CASCADE)
