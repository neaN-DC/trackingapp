from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-small'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input is-small'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-small'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-small'}))
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2',]



class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']




class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']