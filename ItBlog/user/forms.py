from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Գաղտնաբառ",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control'}),

    )
    password2 = forms.CharField(
        label="Գաղտնաբառի հաստատում",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control'}),
    )

    username = forms.CharField(label='Օգտանուն', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'email': 'էլ-հասցե',
        }


class MyUserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Օգտանուն", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Գաղտնաբառ", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
