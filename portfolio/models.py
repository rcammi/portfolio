from datetime import datetime

from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='./portfolio/images/', blank=True)
    short_description = models.CharField(max_length=300, blank=True) 
    description = models.TextField(blank=True)
    link = models.CharField(max_length=300, blank=True)
    date_pub = models.DateTimeField(default=datetime.now, blank=True)

class Blogs(models.Model):
    title = models.CharField(max_length=300)
    short_description = models.CharField(max_length=300, blank=True) 
    link = models.CharField(max_length=300)
    date_pub = models.DateTimeField(default=datetime.now, blank=True)