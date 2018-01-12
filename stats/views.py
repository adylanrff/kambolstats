from django.shortcuts import render
from django.views.generic import ListView

from .models import Player
# Create your views here.

class HomeView(ListView):
    model= Player
    template_name = 'home.html'
