from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'date_of_bitrh', 'password1', 'password2', )
        widgets = {
            'username' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'date_of_bitrh': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            }
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})

class UserProfileForm(forms.ModelForm):
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}),
        required=False,
    )
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'date_of_bitrh', 'password', 'user_image', )
        widgets = { 'date_of_bitrh': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                    'password': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}), }
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
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control', 'disabled': 'disabled'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = False

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description', 'category_image', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Write your description here...', 'class': 'form-control'}),
            'category_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            }
        
    # def __init__(self, *args, **kwargs):
    #     super(CategoryForm, self).__init__(*args, **kwargs)
    #     self.fields['category_image'].required = False