from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.http import HttpResponse
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
        context['home_team_players'] = Player.objects.filter(team=context['home_team'])
        context['away_team'] = Team.objects.get(id = self.object.away_team.id)
        context['away_team_players'] = Player.objects.filter(team=context['away_team'])
        return context
        # class TeamDetailView(ListView):

def update_player(request):
    if request.method == 'POST':
        nim = request.POST['nim'];
        stat_type = request.POST['stat_type']
        operation = request.POST['operation']
        

        player_obj = Player.objects.get(NIM = nim)
        player_update = Player.objects.filter(NIM = nim)

        update_player_stat(stat_type,operation, player_obj, player_update)

        return HttpResponse('')


def update_player_stat(stat_type, operation, player_obj, player_update):
    if (stat_type == 'goal'):
        value = player_obj.goal
        if (operation =='min'):
            value-=1
        player_update.update(goal=value)