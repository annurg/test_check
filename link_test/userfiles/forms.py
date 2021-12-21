from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.models import User
from .models import Client

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    address = forms.CharField(max_length=500,widget=forms.Textarea)


    class Meta:
        model = Client
        fields = ('username', 'email', 'password1', 'password2', 'address')

class UpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=50,)
    email = forms.EmailField(max_length=200, help_text='Required')
    address = forms.CharField(max_length=500,widget=forms.Textarea)

    class Meta:
        model = Client
        fields = ('username', 'email', 'address')

