from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser
from .validators import validate_username, validate_password  # インポートを追加


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        validate_username(username)
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        validate_password(password1)
        return password1


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=150, validators=[validate_username])
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])
