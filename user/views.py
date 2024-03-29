from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, userlistForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		if u_form.is_valid():
			u_form.save()
			messages.success(request, f'Informations has been updated')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
				
	context = {
		'u_form': u_form,
	}
	return render(request, 'user/profile.html', context)

def userlist(request):

	form = userlistForm(request.POST)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		form = userlistForm()
	else:
		print("error")

		
	context = { 'form': form }
	return render (request, 'user/userlist.html', context)