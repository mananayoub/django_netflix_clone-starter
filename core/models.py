from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

def generateUUID():
    return str(uuid4())

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)

MOVIES_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField("Profile", blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=generateUUID)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=generateUUID)
    type = models.CharField(max_length=255, choices=MOVIES_CHOICES)
    videos = models.ManyToManyField("Video")
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)

class Video(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='movies')