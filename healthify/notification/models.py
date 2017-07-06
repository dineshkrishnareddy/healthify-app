from django.db import models

# Create your models here.

class notification(models.Model):
    header = models.CharField(max_length=150,blank=False)
    content = models.CharField(max_length=300,blank=False)
    url = models.CharField(max_length=200,blank=False)
    scheduledTime = models.DateTimeField(blank=False)
    query = models.CharField(max_length=200,blank=False)