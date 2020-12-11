from django import forms
from .models import Post

class HomeForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['player_id',]
