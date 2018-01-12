from django.contrib import admin
from .models import Match, Team, Player

class TeamAdmin(admin.ModelAdmin):
    list_display=['name','points',]

# Register your models here.
admin.site.register(Match)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player)
