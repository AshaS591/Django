from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    tname = models.CharField(max_length=50)
    tdesc = models.TextField()
    tuser = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.tname