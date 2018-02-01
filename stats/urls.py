from django.conf import settings
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    url(r'^login/$', auth_views.login, name ='login'),
    url(r'^logout/$', auth_views.logout, name= 'logout'),
    path('scoreboard/',views.ScoreboardView.as_view(),name='scoreboard'),
    path('teams/',views.TeamListView.as_view(),name='team_list'),
    path('teams/add',views.add_team, name='add_team'),
    path('teams/delete',views.delete_team, name='add_team'),
    path('teams/<int:pk>/',views.TeamDetailView.as_view(), name = 'team_detail'),
    path('match/', views.MatchListView.as_view(), name = 'match_list'),
    path('match/add', views.add_match),
    path('match/delete', views.delete_match),
    path('match/start', views.start_timer),
    path('match/stop', views.stop_timer),
    path('match/<int:pk>/ingame',views.MatchInGameView.as_view(), name ='match_in_game'),
    path('match/evaluate',views.evaluate_match),
    path('players/update/',views.update_stats),
    path('players/add',views.add_player, name='add_player'),
    path('players/delete',views.delete_player, name='delete_player'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)