from .models import Team, Match, Player
from django import forms
from django.contrib.admin import widgets

class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = [
			"name",
			"logo",
		]

class MatchForm(forms.ModelForm):
	class Meta:
		model = Match
		fields = [
			"match_date",
			"home_team",
			"away_team",
		]

	def __init__(self, *args, **kwargs):
		super(MatchForm, self).__init__(*args, **kwargs)
		self.fields['match_date'].widget = widgets.AdminSplitDateTime()

class PlayerForm(forms.ModelForm):
	class Meta:
		model = Player
		fields = [
			"NIM",
			"name",
			"height",
			"weight",
			"team",
			"ktm_photo",
			"player_photo",
		]