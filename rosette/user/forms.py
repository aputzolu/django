from django import forms

class UserForm(forms.Form):
	username = forms.CharField(max_length=100)
	company = forms.CharField(max_length=100)
	mail = forms.CharField(max_length=100)
	mdp = forms.CharField(max_length=100)