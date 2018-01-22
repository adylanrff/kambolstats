from django.db import models

# Create your models here.

class Team(models.Model):
    class Meta:
        ordering = ['-points',]

    # Stats
    name = models.TextField()
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
    available = models.BooleanField()
    
    # home
    goal_home = models.IntegerField(default=0)
    pass_complete_home = models.IntegerField(default=0)
    pass_incomplete_home = models.IntegerField(default=0)
    ball_possession_home = models.IntegerField(default=0)
    shot_on_target_home = models.IntegerField(default=0)
    shot_off_target_home = models.IntegerField(default=0)
    shot_percentage_home = models.DecimalField(max_digits = 4, decimal_places = 2, default=0)
    intercept_home = models.IntegerField(default=0)
    block_home = models.IntegerField(default=0)
    clearance_home = models.IntegerField(default=0)
    ball_recovery_home = models.IntegerField(default=0)
    saves_home = models.IntegerField(default=0)
    tackle_home = models.IntegerField(default=0)
    second_ball_home = models.IntegerField(default=0)
    fouls_committed_home = models.IntegerField(default=0)
    fouls_suffered_home = models.IntegerField(default=0)
    yellow_card_home = models.IntegerField(default=0)
    red_card_home = models.IntegerField(default=0)
    free_kick_home = models.IntegerField(default=0)
    penalty_kick_home = models.IntegerField(default=0)
    
    # away
    goal_away = models.IntegerField(default=0)
    pass_complete_away = models.IntegerField(default=0)
    pass_incomplete_away = models.IntegerField(default=0)
    ball_possession_away = models.IntegerField(default=0)
    shot_on_target_away = models.IntegerField(default=0)
    shot_off_target_away = models.IntegerField(default=0)
    shot_percentage_away = models.DecimalField(max_digits = 4, decimal_places = 2, default=0)
    intercept_away = models.IntegerField(default=0)
    block_away = models.IntegerField(default=0)
    clearance_away = models.IntegerField(default=0)
    ball_recovery_away = models.IntegerField(default=0)
    saves_away = models.IntegerField(default=0)
    tackle_away = models.IntegerField(default=0)
    second_ball_away = models.IntegerField(default=0)
    fouls_committed_away = models.IntegerField(default=0)
    fouls_suffered_away = models.IntegerField(default=0)
    yellow_card_away = models.IntegerField(default=0)
    red_card_away = models.IntegerField(default=0)
    free_kick_away = models.IntegerField(default=0)
    penalty_kick_away = models.IntegerField(default=0)


    def __str__(self):
        return str(self.id)

class Player(models.Model):
    class Meta:
        ordering = ['NIM',]

    NIM = models.IntegerField(primary_key=True)
    name = models.TextField()
    team = models.ForeignKey(Team, related_name="team", on_delete=models.CASCADE, null=True)

    # Stats
    goal = models.IntegerField(default=0)
    pass_complete = models.IntegerField(default=0)
    pass_incomplete = models.IntegerField(default=0)
    ball_possession = models.IntegerField(default=0)
    shot_on_target = models.IntegerField(default=0)
    shot_off_target = models.IntegerField(default=0)
    shot_percentage = models.DecimalField(max_digits = 4, decimal_places = 2, default=0)
    intercept = models.IntegerField(default=0)
    block = models.IntegerField(default=0)
    clearance = models.IntegerField(default=0)
    ball_recovery = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    tackle = models.IntegerField(default=0)
    second_ball = models.IntegerField(default=0)
    fouls_committed = models.IntegerField(default=0)
    fouls_suffered = models.IntegerField(default=0)
    yellow_card = models.IntegerField(default=0)
    red_card = models.IntegerField(default=0)
    free_kick = models.IntegerField(default=0)
    penalty_kick = models.IntegerField(default=0)


    def __str__(self):
        return self.name
