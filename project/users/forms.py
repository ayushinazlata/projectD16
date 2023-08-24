from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Имя пользователя')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


class ActivateForm(forms.Form):
    code = forms.CharField(label='код активации')


