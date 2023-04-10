from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegForm(UserCreationForm):
    username = forms.CharField(label='Your UserID:', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control-plaintext',
               'placeholder': 'UserID',
               'id': 'userid',
               'required': 'true',
               'readonly': 'readonly'}))
    first_name = forms.CharField(label='First Name', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'First Name',
               'id': 'firstname',
               'required': 'true'}))
    last_name = forms.CharField(label='Last Name', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Last Name',
               'id': 'lastname',
               'required': 'true'}))
    email = forms.CharField(label = 'E-Mail', max_length=30, widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'placeholder': 'E-Mail',
               'id': 'email',
               'required': 'true'}))
    password1 = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'Password',
               'id': 'password1',
               'required': 'true'}))
    password2 = forms.CharField(label='Repeat Password', max_length=30, widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'Repeat Password',
               'id': 'password2',
               'required': 'true'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2','username' )


class CustomAuthenticationForm(AuthenticationForm):
        username = forms.CharField(label='UserID', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'UserID',
               'id': 'userid',
               'required': 'true'}))
        password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'Password',
               'id': 'password',
               'required': 'true'}))