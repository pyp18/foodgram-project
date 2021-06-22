from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Optional', error_messages={'required': 'Никнейм обязателен'})
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional', error_messages={'required': 'Имя обязательно'})
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address', error_messages={'required': 'Почта должна быть корректной'})
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput, error_messages={'required': 'Почта должна быть корректной'})
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput, error_messages={'required': 'Почта должна быть корректной'},
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'email', 
            'password1', 
            'password2', 
            ]