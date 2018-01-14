from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('scoreboard/',views.ScoreboardView.as_view(),name='scoreboard'),
    path('teams/<int:pk>/',views.TeamDetailView.as_view(), name = 'team_detail'),
    # path('match/<int:pk>/',views.MatchInGameView.as_view(), name ='match_in_game')
    path('match/<int:pk>/ingame',views.MatchInGameView.as_view(), name ='match_in_game')
]
