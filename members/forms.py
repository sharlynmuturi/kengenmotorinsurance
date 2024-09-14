from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# class RegisterUserForm(UserCreationForm):
# 	firstname = forms.CharField(max_length=100)
# 	lastname = forms.CharField(max_length=100)
# 	email = forms.EmailField()

# 	class Meta:
# 		model = User
# 		fields = ('username', 'firstname', 'lastname', 'email', 'password1', 'password2')