from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Player, Team
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class ScoreboardView(ListView):
    model = Team
    template_name = 'scoreboard.html'

# class TeamDetailView(ListView):
