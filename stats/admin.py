from django.contrib import admin
from .models import Match, Team, Player

class TeamAdmin(admin.ModelAdmin):
    list_display=['name','points',]

class PlayerAdmin(admin.ModelAdmin):
    list_display=['NIM','name','goals','shoot','pass_succees','pass_unsuccess']

class MatchAdmin(admin.ModelAdmin):
    list_display = ['id','home_team','away_team','match_date']

# Register your models here.
admin.site.register(Match, MatchAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
