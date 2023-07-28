from django.shortcuts import render
from .models import Agent, Command


# Create your views here.

def index(request):
    agents = Agent.objects.all()

    for agent in agents:
        agent.command_list = agent.commands.all()

    context = {
        'agents': agents,
    }

    return render(request, context=context, template_name='C2/index.html')