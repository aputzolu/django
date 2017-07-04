from django import forms
from .models import Company
from user.models import UserProfile

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="")
    renvoi = forms.BooleanField(help_text="", required=False)

    from django import forms

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class UserForm(forms.Form):
	name = forms.CharField(max_length=100)
	company = forms.CharField(max_length=100)
