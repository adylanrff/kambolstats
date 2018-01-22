from django.contrib import admin
from .models import Match, Team, Player

class TeamAdmin(admin.ModelAdmin):
    pass
    list_display=['name','points',]
# 
class PlayerAdmin(admin.ModelAdmin):
    pass
    list_display=['NIM','name','goal','shot_on_target','shot_off_target','shot_percentage','pass_complete','pass_incomplete']

class MatchAdmin(admin.ModelAdmin):
    pass
    list_display = ['id','home_team','away_team','match_date']

# Register your models here.
admin.site.register(Match, MatchAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
