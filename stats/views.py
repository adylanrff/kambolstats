from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse
from .models import Player, Team, Match
from .forms import TeamForm, MatchForm, PlayerForm
# Create your views here.

class FormListView(FormMixin, ListView):
    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        # From BaseListView
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})

        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

class HomeView(TemplateView):
    template_name = 'home.html'

class ScoreboardView(ListView):
    model = Team
    context_object_name = 'team_list'
    template_name = 'scoreboard.html'

class TeamListView(FormListView):
    form_class = TeamForm
    model = Team
    context_object_name = 'team_list'
    template_name = 'team_list.html'

class TeamDetailView(DetailView):
    form_class = PlayerForm
    model = Team
    context_object_name = 'team'
    template_name = 'team_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['player_list'] = Player.objects.filter(team = self.object)
        context['form'] = PlayerForm
        return context


class MatchListView(FormListView):
    form_class = MatchForm
    model = Match
    context_object_name = 'match_list'
    template_name = 'match_list.html'


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

def add_team(request):
    form = TeamForm(data = request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponse('')
    else:
        print(form.errors)
        # name = request.POST['name']
        # Team.objects.create(name=name).save()
    return HttpResponse('')

def add_match(request):
    if (request.method =='POST'):
        home_team_id = request.POST['home_team_id']
        away_team_id = request.POST['away_team_id']
        match_date = request.POST['match_date']
        match_time = request.POST['match_time']

        home_team = Team.objects.get(id=home_team_id)
        away_team = Team.objects.get(id=away_team_id)
        match_datetime = match_date + " " + match_time
        
        Match.objects.create(home_team = home_team, away_team=away_team, match_date = match_datetime, available=True)


    return HttpResponse('')

def add_player(request):
    form = PlayerForm(data = request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponse('')
    else:
        print(form.errors)
        # name = request.POST['name']
        # Team.objects.create(name=name).save()
    return HttpResponse('')


def update_stats(request):
    if request.method == 'POST':
        nim = request.POST['nim']
        stat_type = request.POST['stat_type']
        operation = request.POST['operation']
        match_id = request.POST['match_id']
        side = request.POST['side']
        home_team_id = request.POST['home_team_id']
        away_team_id = request.POST['away_team_id']

        player_obj = Player.objects.get(NIM = nim)
        player_update = Player.objects.filter(NIM = nim)

        match_obj = Match.objects.get(id=match_id)
        match_update = Match.objects.filter(id = match_id)

        update_player_stat(stat_type,operation, player_obj, player_update)
        update_match_stat(stat_type,operation,match_obj,match_update,side)
        update_team_stat(stat_type,operation,home_team_id,away_team_id,side)

        return HttpResponse('')

    # if request.method == 'GET':

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

        pass_complete_away = value
        pass_complete_home = match_obj.pass_complete_home

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

def update_team_stat(stat_type, operation, home_team_id, away_team_id,side):
    home_team_obj = Team.objects.get(id = home_team_id)
    home_team_update = Team.objects.filter(id=home_team_id)
    
    away_team_obj = Team.objects.get(id = away_team_id)
    away_team_update = Team.objects.filter(id=away_team_id)

    if (operation =='min'):
        value= -1
    elif (operation =='plus'):
        value= 1
    else:
        value = 0

    if (side=='away'):
        if (stat_type == 'goal'):
            goal_for_away = value+away_team_obj.goal_for
            goal_against_home = value+ home_team_obj.goal_against
            away_team_update.update(goal_for=goal_for_away)
            home_team_update.update(goal_against= goal_against_home)
    else:
        if (stat_type == 'goal'):
            goal_for_home = value + home_team_obj.goal_for
            goal_against_away = value+ away_team_obj.goal_against
            home_team_update.update(goal_for=goal_for_home)
            away_team_update.update(goal_against= goal_against_away)

def evaluate_match(request):
    if (request.method=='POST'):
        match_id = request.POST['match_id']
        home_team_id = request.POST['home_team_id']
        away_team_id = request.POST['away_team_id']
        goal_home = request.POST['goal_home']
        goal_team = request.POST['goal_away']

        match = Match.objects.filter(id = match_id)

        home_team_obj = Team.objects.get(id = home_team_id)
        home_team_update = Team.objects.filter(id = home_team_id)


        away_team_obj = Team.objects.get(id = away_team_id)
        away_team_update = Team.objects.filter(id = away_team_id)

        match.update(available = False)

        if (goal_home>goal_team):
            win_home = home_team_obj.win
            win_home+=1

            lose_away = away_team_obj.lose
            lose_away+=1

            home_team_update.update(win = win_home)
            away_team_update.update(lose = lose_away)

        elif (goal_home<goal_team):
            win_away = away_team_obj.win
            win_away+=1

            lose_home = home_team_obj.lose
            lose_home+=1

            home_team_update.update(lose = lose_home)
            away_team_update.update(win = win_away)
        else:
            draw_home = home_team_obj.draw
            draw_away = away_team_obj.draw
            draw_home+=1
            draw_away+=1

            home_team_update.update(draw = draw_home)
            away_team_update.update(draw = draw_away)

    return HttpResponse('')