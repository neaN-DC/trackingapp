from django import forms
from .models import UsersId

class HomeForm(forms.ModelForm):
	class Meta:
		model = UsersId
		fields = ['players_name_given','player_id', 'playersteam_id', ]