from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First name')
    last_name = forms.CharField(max_length=100, help_text='Last name')
    university = forms.CharField(max_length=300, required=False, help_text='University name')
    university_username = forms.CharField(max_length=100, required=False, help_text='University account username')
    university_password = forms.CharField(max_length=100, required=False, help_text='University account password', widget=forms.PasswordInput)
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'university', 'university_username', 'university_password', 'password1', 'password2')