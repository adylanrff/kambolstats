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
        match_id = request.POST['match_id']
        side = request.POST['side']

        player_obj = Player.objects.get(NIM = nim)
        player_update = Player.objects.filter(NIM = nim)
        
        match_obj = Match.objects.get(id=match_id)
        match_update = Match.objects.filter(id = match_id)

        update_player_stat(stat_type,operation, player_obj, player_update)
        update_match_stat(stat_type,operation,match_obj,match_update,side)

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

    elif (stat_type == 'pass_complete'):
        value+= player_obj.pass_complete
        player_update.update(pass_complete=value)

    elif (stat_type == 'pass_incomplete'):
        value+= player_obj.pass_incomplete
        player_update.update(pass_incomplete=value)

    elif (stat_type == 'shot_on_target'):
        value+= player_obj.shot_on_target
        player_update.update(shot_on_target=value)

        shot_on_target = value
        shot_off_target = player_obj.shot_off_target

        if (shot_on_target+shot_off_target>0):
            percentage = (shot_on_target / (shot_on_target+shot_off_target)) *100
        else:
            percentage = 0

        print(shot_on_target)
        print(shot_off_target)
        print(percentage)

        player_update.update(shot_percentage=percentage)

    elif (stat_type == 'shot_off_target'):
        value += player_obj.shot_off_target
        player_update.update(shot_off_target=value)

        shot_on_target = player_obj.shot_on_target
        shot_off_target = value

        if (shot_on_target+shot_off_target>0):
            percentage = (shot_on_target / (shot_on_target+shot_off_target)) *100
        else:
            percentage = 0

        print(shot_on_target)
        print(shot_off_target)
        print(percentage)

        player_update.update(shot_percentage=percentage)

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

def update_match_stat(stat_type, operation, match_obj, match_update,side):
    if (operation =='min'):
        value= -1
    elif (operation =='plus'):
        value= 1
    else:
        value = 0

    if (side == 'home'):
        update_match_home(stat_type, operation, match_obj, match_update, value)
    else:
        update_match_away(stat_type, operation, match_obj, match_update, value)

def update_match_home(stat_type, operation, match_obj, match_update, value):
    if (stat_type == 'goal'):
        value += match_obj.goal_home   
        match_update.update(goal_home=value)


    elif (stat_type == 'pass_complete'):
        value+= match_obj.pass_complete_home
        match_update.update(pass_complete_home=value)

        pass_complete_away = match_obj.pass_complete_away
        pass_complete_home = value

        if (pass_complete_home+pass_complete_away>0):
            possession_home = pass_complete_home / (pass_complete_home+pass_complete_away) *100
            possession_away = pass_complete_away / (pass_complete_home+pass_complete_away) *100

        else:
            passession_home = 0 
            passession_away = 0 

        match_update.update(ball_possession_home=possession_home)
        match_update.update(ball_possession_away=possession_away)

    elif (stat_type == 'pass_incomplete'):
        value+= match_obj.pass_incomplete_home
        match_update.update(pass_incomplete_home=value)

    elif (stat_type == 'shot_on_target'):
        value+= match_obj.shot_on_target_home
        match_update.update(shot_on_target_home=value)

    elif (stat_type == 'shot_off_target'):
        value += match_obj.shot_off_target_home
        match_update.update(shot_off_target_home=value)

    elif (stat_type == 'intercept'):
        value += match_obj.intercept_home
        match_update.update(intercept_home=value)

    elif (stat_type == 'block'):
        value += match_obj.block_home
        match_update.update(block_home=value)
    
    elif (stat_type == 'clearance'):
        value += match_obj.clearance_home
        match_update.update(clearance_home=value)
    
    elif (stat_type == 'ball_recovery'):
        value += match_obj.ball_recovery_home
        match_update.update(ball_recovery_home=value)
    
    elif (stat_type == 'saves'):
        value += match_obj.saves_home
        match_update.update(saves_home=value)
    
    elif (stat_type == 'tackle'):
        value += match_obj.tackle_home
        match_update.update(tackle_home=value)
    
    elif (stat_type == 'second_ball'):
        value += match_obj.second_ball_home
        match_update.update(second_ball_home=value)
    
    elif (stat_type == 'fouls_committed'):
        value += match_obj.fouls_committed_home
        match_update.update(fouls_committed_home=value)
    
    elif (stat_type == 'fouls_suffered'):
        value += match_obj.fouls_suffered_home
        match_update.update(fouls_suffered_home=value)
    
    elif (stat_type == 'yellow_card'):
        value += match_obj.yellow_card_home
        match_update.update(yellow_card_home=value)
    
    elif (stat_type == 'red_card'):
        value += match_obj.red_card_home
        match_update.update(red_card_home=value)
    
    elif (stat_type == 'free_kick'):
        value += match_obj.free_kick_home
        match_update.update(free_kick_home=value)
    
    elif (stat_type == 'penalty_kick'):
        value += match_obj.penalty_kick_home
        match_update.update(penalty_kick_home=value)

def update_match_away(stat_type, operation, match_obj, match_update, value):
    if (stat_type == 'goal'):
        value += match_obj.goal_away   
        match_update.update(goal_away=value)

    elif (stat_type == 'shot_on_target'):
        value+= match_obj.shot_on_target_away
        match_update.update(shot_on_target_away=value)

    elif (stat_type == 'pass_complete'):
        value+= match_obj.pass_complete_away
        match_update.update(pass_complete_away=value)

        pass_complete_away = match_obj.pass_complete_away
        pass_complete_home = value

        if (pass_complete_home+pass_complete_away>0):
            possession_home = pass_complete_home / (pass_complete_home+pass_complete_away) *100
            possession_away = pass_complete_away / (pass_complete_home+pass_complete_away) *100

        else:
            passession_home = 0 
            passession_away = 0 

        match_update.update(ball_possession_home=possession_home)
        match_update.update(ball_possession_away=possession_away)


    elif (stat_type == 'pass_incomplete'):
        value+= match_obj.pass_incomplete_away
        match_update.update(pass_incomplete_away=value)

    elif (stat_type == 'shot_off_target'):
        value += match_obj.shot_off_target_away
        match_update.update(shot_off_target_away=value)

    elif (stat_type == 'intercept'):
        value += match_obj.intercept_away
        match_update.update(intercept_away=value)

    elif (stat_type == 'block'):
        value += match_obj.block_away
        match_update.update(block_away=value)
    
    elif (stat_type == 'clearance'):
        value += match_obj.clearance_away
        match_update.update(clearance_away=value)
    
    elif (stat_type == 'ball_recovery'):
        value += match_obj.ball_recovery_away
        match_update.update(ball_recovery_away=value)
    
    elif (stat_type == 'saves'):
        value += match_obj.saves_away
        match_update.update(saves_away=value)
    
    elif (stat_type == 'tackle'):
        value += match_obj.tackle_away
        match_update.update(tackle_away=value)
    
    elif (stat_type == 'second_ball'):
        value += match_obj.second_ball_away
        match_update.update(second_ball_away=value)
    
    elif (stat_type == 'fouls_committed'):
        value += match_obj.fouls_committed_away
        match_update.update(fouls_committed_away=value)
    
    elif (stat_type == 'fouls_suffered'):
        value += match_obj.fouls_suffered_away
        match_update.update(fouls_suffered_away=value)
    
    elif (stat_type == 'yellow_card'):
        value += match_obj.yellow_card_away
        match_update.update(yellow_card_away=value)
    
    elif (stat_type == 'red_card'):
        value += match_obj.red_card_away
        match_update.update(red_card_away=value)
    
    elif (stat_type == 'free_kick'):
        value += match_obj.free_kick_away
        match_update.update(free_kick_away=value)
    
    elif (stat_type == 'penalty_kick'):
        value += match_obj.penalty_kick_away
        match_update.update(penalty_kick_away=value)
