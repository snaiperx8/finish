from django import forms
from django.contrib.auth.models import User
from apps.models import CreatePost

class Create_entry_form(forms.ModelForm):
	class Meta:
		model = CreatePost
		exclude = ['autor', 'date']
		
class Sign_up_form(forms.ModelForm):
	username = forms.CharField(max_length = 100)
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = User
		fields = ['username', 'password', 'email']