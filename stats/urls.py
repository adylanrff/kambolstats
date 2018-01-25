from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('scoreboard/',views.ScoreboardView.as_view(),name='scoreboard'),
    path('teams/',views.TeamListView.as_view(),name='team_list'),
    path('teams/add',views.add_team, name='add_team'),
    path('teams/<int:pk>/',views.TeamDetailView.as_view(), name = 'team_detail'),
    path('match/', views.MatchListView.as_view(), name = 'match_list'),
    path('match/add', views.add_match),
    path('match/<int:pk>/ingame',views.MatchInGameView.as_view(), name ='match_in_game'),
    path('match/evaluate',views.evaluate_match),
    path('players/update/',views.update_stats),
    path('players/add',views.add_player, name='add_player'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)