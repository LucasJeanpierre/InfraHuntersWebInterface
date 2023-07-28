from django.db import models

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    last_online = models.DateTimeField()
    host = models.CharField(max_length=50)  
    ip = models.CharField(max_length=50)
    port = models.IntegerField()
    os = models.CharField(max_length=50)
    os_version = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    commands = models.ManyToManyField('Command', blank=True)

    def __str__(self):
        return self.name


class Command(models.Model):
    name = models.CharField(max_length=50)
    syntax = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name