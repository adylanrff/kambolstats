from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from .models import Player, Team
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class ScoreboardView(ListView):
    model = Team
    context_object_name = 'team_list'
    template_name = 'scoreboard.html'

class TeamDetailView(DetailView):
    model = Team
    context_object_name = 'team'
    template_name = 'team_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['player_list'] = Player.objects.filter(team = self.object) 
        return context
# class TeamDetailView(ListView):
