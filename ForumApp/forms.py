from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'date_of_bitrh', )
        widgets = { 'date_of_bitrh': forms.DateInput(attrs={'type': 'date', 'class': ''}), }

class UserProfileForm(forms.ModelForm):
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={'class': ''}),
        required=False,
    )
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'date_of_bitrh', 'password', 'user_image', )
        widgets = { 'date_of_bitrh': forms.DateInput(attrs={'type': 'date', 'class': ''}),
                    'password': forms.PasswordInput(), }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            self.add_error("password2", "Пароли не совпадают.")

        if password:
            try:
                validate_password(password)
            except ValidationError as e:
                self.add_error("password", e.messages[0])

        return cleaned_data