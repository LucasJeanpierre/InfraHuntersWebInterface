from django.contrib import admin
from .models import Agent, Command, AgentType

# Register your models here.
admin.site.register(Agent)
admin.site.register(Command)
admin.site.register(AgentType)
