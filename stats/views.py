from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from .models import Player, Team, Match
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

class MatchInGameView(DetailView):
    model = Match
    context_object_name = 'match'
    template_name = 'match_in_game.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_team'] = Team.objects.get(id = self.object.home_team.id)
        context['away_team'] = Team.objects.get(id = self.object.away_team.id)
        return context
        # class TeamDetailView(ListView):
