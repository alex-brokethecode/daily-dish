from django import forms
# from django.contrib.auth.forms import AuthenticationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2 mt-4',
                'placeholder': 'Username',
            }
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-2 mt-4',
                'placeholder': 'Password',
            }
        )
    )
