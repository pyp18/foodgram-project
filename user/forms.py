from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional', error_messages={'required': 'Имя обязательно'})
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address', error_messages={'required': 'Почта должна быть корректной'})

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'email', 
            'password1', 
            'password2', 
            ]