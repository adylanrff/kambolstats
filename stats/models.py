from django.db import models

# Create your models here.

class Team(models.Model):
    class Meta:
        ordering = ['-points',]

    # Stats
    name = models.TextField()
    points = models.IntegerField(default=0)

    # goals conceded
    # goals
    def __str__(self):
        return self.name

class Match(models.Model):
    class Meta:
        ordering = ['-match_date',]

    match_date = models.DateTimeField()
    home_team = models.ForeignKey(Team, related_name="home_team", on_delete=models.CASCADE, null=True)
    away_team = models.ForeignKey(Team, related_name="away_team", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)

class Player(models.Model):
    class Meta:
        ordering = ['NIM',]

    NIM = models.IntegerField(primary_key=True)
    name = models.TextField()
    team = models.ForeignKey(Team, related_name="team", on_delete=models.CASCADE, null=True)
    # Stats
    goals = models.IntegerField(default=0)
    shoot = models.IntegerField(default=0)
    pass_succees = models.IntegerField(default=0)
    pass_unsuccess = models.IntegerField(default=0)

    def __str__(self):
        return self.name
