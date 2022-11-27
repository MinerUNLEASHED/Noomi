from django import forms
from django.contrib.auth.models import User
from django.core import validators

class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(100)])
    username = forms.CharField(validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(100)])
    email = forms.CharField(validators=[validators.MaxLengthValidator(100)])
    
    class Meta():
        model = User
        fields = ('username','email','password')

