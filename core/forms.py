from django import forms
from .models import UsersIds

class HomeForm(forms.ModelForm):
	class Meta:
		model = UsersIds
		fields = ['name','player_id', ]
