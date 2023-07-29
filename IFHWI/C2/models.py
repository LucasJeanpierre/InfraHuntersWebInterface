from django.db import models

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    last_online = models.DateTimeField(null=True, blank=True)
    host = models.CharField(max_length=50, null=True, blank=True)  
    ip = models.CharField(max_length=50, null=True, blank=True)
    port = models.IntegerField(null=True, blank=True)
    uid = models.CharField(max_length=50, null=True, blank=True)
    guid = models.CharField(max_length=50, null=True, blank=True)
    os = models.CharField(max_length=50, null=True, blank=True)
    os_version = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey('AgentType', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class AgentType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True, blank=True)
    commands = models.ManyToManyField('Command', blank=True)

    def __str__(self):
        return self.name
    

class Command(models.Model):
    name = models.CharField(max_length=50)
    syntax = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name