from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('scoreboard/',views.ScoreboardView.as_view(),name='scoreboard')
    
]
