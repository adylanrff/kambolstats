from django.db import models

# Create your models here.
class Match(models.Model):
    class Meta:
        ordering = ['-date',]
    match_date = models.DateTimeField()
    home = models.ManyToManyField(Team)
    away = models.ManyToManyField(Team)

class Team(models.Model):
    class Meta:
        ordering = ['-points',]

    # Stats
    name = models.TextField()
    points = models.IntegerField()



class Player(models.Model):
    class Meta:
        ordering = ['NIM',]

    NIM = models.IntegerField(primary_key=True)
    name = models.TextField()

    # Stats
    goals = models.IntegerField()
    shoot = models.IntegerField()
    pass_succees = models.IntegerField()
    pass_unsuccess = models.IntegerField()

    def __str__(self):
        return self.name
