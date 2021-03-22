from django import forms
from .models import UsersId

class HomeForm(forms.ModelForm):
	class Meta:
		model = UsersId
		fields = ['players_name_given','player_id', 'playersteam_id', ]


		widgets = {
			'players_name_given': forms.TextInput(attrs={'class': 'input is-small'}),
			'player_id': forms.TextInput(attrs={'class': 'input is-small'}),
			'playersteam_id': forms.TextInput(attrs={'class': 'input is-small'}),
		}