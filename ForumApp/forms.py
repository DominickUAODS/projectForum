from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'date_of_bitrh', )
        widgets = { 'date_of_bitrh': forms.DateInput(attrs={'type': 'date', 'class': ''}), }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'date_of_bitrh', 'password', 'user_image', )
        widgets = { 'date_of_bitrh': forms.DateInput(attrs={'type': 'date', 'class': ''}),
                    'password': forms.PasswordInput(), }