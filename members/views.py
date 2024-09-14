from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# from .forms import RegisterUserForm

# Create your views here.
def loginuser(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
		    login(request, user)
		    return redirect ('home')
		else:
			messages.success(request, ("Log Out Error! Try again"))
			return redirect ('loginuser')

	else:
		return render(request, 'loginuser.html',{})

def logoutuser(request):
	logout(request)
	messages.success(request, ("Log Out Success"))
	return redirect ('home')

def registeruser(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('home')
	else:
			form = UserCreationForm()
	return render(request, 'registeruser.html', {'form': form})
