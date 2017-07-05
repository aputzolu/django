from django import forms
from .models import Company
from user.models import UserProfile

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    envoyeur = forms.EmailField(label="")
    renvoi = forms.BooleanField(help_text="", required=False)

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'