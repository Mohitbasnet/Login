from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
class RegistrationForm(UserCreationForm):
    # Add any additional fields you want here
    class Meta:
        model = CustomUser  # Your custom user model
        fields = ['username', 'email']

class LoginForm(AuthenticationForm):
    pass