from django import forms
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError

from accounts.models import User


class SignInForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise ValidationError('Incorrect credentials')


class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not password == confirm_password:
            raise ValidationError('Passwords doesn\'t match.')
