from django.db import models

# Create your models here.

class Team(models.Model):
    class Meta:
        ordering = ['-win','-draw','-lose','-goal_for','-goal_against']

    # Stats
    name = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True)
    points = models.IntegerField(default=0)
    goal_for = models.IntegerField(default=0)
    goal_against = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Match(models.Model):
    class Meta:
        ordering = ['-match_date',]

    match_date = models.DateTimeField()
    home_team = models.ForeignKey(Team, related_name="home_team", on_delete=models.CASCADE, null=True)
    away_team = models.ForeignKey(Team, related_name="away_team", on_delete=models.CASCADE, null=True)
    time_started = models.BooleanField(default=False)
    match_time = models.DateTimeField(auto_now_add=True)
    
    available = models.BooleanField()
    # home
    goal_home = models.IntegerField(default=0)
    pass_complete_home = models.IntegerField(default=0)
    pass_incomplete_home = models.IntegerField(default=0)
    ball_possession_home = models.DecimalField(max_digits = 5, decimal_places = 2, default=0)
    shot_on_target_home = models.IntegerField(default=0)
    shot_off_target_home = models.IntegerField(default=0)
    shot_percentage_home = models.DecimalField(max_digits = 5, decimal_places = 2, default=0)
    intercept_home = models.IntegerField(default=0)
    saves_home = models.IntegerField(default=0)
    tackle_home = models.IntegerField(default=0)
    fouls_committed_home = models.IntegerField(default=0)
    fouls_suffered_home = models.IntegerField(default=0)
    yellow_card_home = models.IntegerField(default=0)
    red_card_home = models.IntegerField(default=0)

    # away
    goal_away = models.IntegerField(default=0)
    pass_complete_away = models.IntegerField(default=0)
    pass_incomplete_away = models.IntegerField(default=0)
    ball_possession_away = models.DecimalField(max_digits = 5, decimal_places = 2, default=0)
    shot_on_target_away = models.IntegerField(default=0)
    shot_off_target_away = models.IntegerField(default=0)
    shot_percentage_away = models.DecimalField(max_digits = 5, decimal_places = 2, default=0)
    intercept_away = models.IntegerField(default=0)
    saves_away = models.IntegerField(default=0)
    tackle_away = models.IntegerField(default=0)
    fouls_committed_away = models.IntegerField(default=0)
    fouls_suffered_away = models.IntegerField(default=0)
    yellow_card_away = models.IntegerField(default=0)
    red_card_away = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

class Player(models.Model):
    class Meta:
        ordering = ['NIM',]

    NIM = models.IntegerField(primary_key=True)
    player_number = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    player_photo = models.ImageField(upload_to ='uploads/player/photo', null=True, blank=True)
    ktm_photo = models.ImageField(upload_to ='uploads/player/ktm', null=True, blank=True)
    team = models.ForeignKey(Team, related_name="team", on_delete=models.CASCADE, null=True)

    # Stats
    goal = models.IntegerField(default=0)
    pass_complete = models.IntegerField(default=0)
    pass_incomplete = models.IntegerField(default=0)
    shot_on_target = models.IntegerField(default=0)
    shot_off_target = models.IntegerField(default=0)
    shot_percentage = models.DecimalField(max_digits = 5, decimal_places = 2, default=0)
    intercept = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    tackle = models.IntegerField(default=0)
    fouls_committed = models.IntegerField(default=0)
    fouls_suffered = models.IntegerField(default=0)
    yellow_card = models.IntegerField(default=0)
    red_card = models.IntegerField(default=0)

    def __str__(self):
        return self.name
