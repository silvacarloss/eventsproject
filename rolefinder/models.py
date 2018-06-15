from django.db import models
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class User(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=70)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField()
    address = models.CharField(max_length = 200)
    date = models.DateTimeField("event datetime")
    picture = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    def __str__(self):
        return self.title

    def happens_soon(self):
        return self.date >= timezone.now() + datetime.timedelta(days=7)

class EventTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)

class UserTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
