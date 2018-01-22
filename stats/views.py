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
        nim = request.POST['nim']
        stat_type = request.POST['stat_type']
        operation = request.POST['operation']

        player_obj = Player.objects.get(NIM = nim)
        player_update = Player.objects.filter(NIM = nim)
        
        update_player_stat(stat_type,operation, player_obj, player_update)

        return HttpResponse('')


def update_player_stat(stat_type, operation, player_obj, player_update):
    
    if (operation =='min'):
        value= -1
    elif (operation =='plus'):
        value= 1
    else:
        value = 0

    if (stat_type == 'goal'):
        value += player_obj.goal    
        player_update.update(goal=value)

    elif (stat_type == 'shot_on_target'):
        value+= player_obj.shot_on_target
        player_update.update(shot_on_target=value)

    elif (stat_type == 'shot_off_target'):
        value += player_obj.shot_off_target
        player_update.update(shot_off_target=value)

    elif (stat_type == 'shot_percentage'):
        value += player_obj.shot_percentage
        player_update.update(shot_percentage=value)

    elif (stat_type == 'intercept'):
        value += player_obj.intercept
        player_update.update(intercept=value)

    elif (stat_type == 'block'):
        value += player_obj.block
        player_update.update(block=value)
    
    elif (stat_type == 'clearance'):
        value += player_obj.clearance
        player_update.update(clearance=value)
    
    elif (stat_type == 'ball_recovery'):
        value += player_obj.ball_recovery
        player_update.update(ball_recovery=value)
    
    elif (stat_type == 'saves'):
        value += player_obj.saves
        player_update.update(saves=value)
    
    elif (stat_type == 'tackle'):
        value += player_obj.tackle
        player_update.update(tackle=value)
    
    elif (stat_type == 'second_ball'):
        value += player_obj.second_ball
        player_update.update(second_ball=value)
    
    elif (stat_type == 'fouls_committed'):
        value += player_obj.fouls_committed
        player_update.update(fouls_committed=value)
    
    elif (stat_type == 'fouls_suffered'):
        value += player_obj.fouls_suffered
        player_update.update(fouls_suffered=value)
    
    elif (stat_type == 'yellow_card'):
        value += player_obj.yellow_card
        player_update.update(yellow_card=value)
    
    elif (stat_type == 'red_card'):
        value += player_obj.red_card
        player_update.update(red_card=value)
    
    elif (stat_type == 'free_kick'):
        value += player_obj.free_kick
        player_update.update(free_kick=value)
    
    elif (stat_type == 'penalty_kick'):
        value += player_obj.penalty_kick
        player_update.update(penalty_kick=value)

