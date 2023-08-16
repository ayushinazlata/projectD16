from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.mail import EmailMultiAlternatives

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

    # def save(self):
    #     user = super().save()
    #
    #     subject = 'Добро пожаловать на портал!'
    #     text = f'{user.username}, вы успешно зарегистрировались на сайте!'
    #     html = (
    #         f'<b>{user.username}</b>, вы успешно зарегистрировались на '
    #         f'<a href="http://127.0.0.1:8000/adverts">сайте</a>!'
    #     )
    #     msg = EmailMultiAlternatives(
    #         subject=subject, body=text, from_email=None, to=[user.email]
    #     )
    #     msg.attach_alternative(html, "text/html")
    #     msg.send()
    #
    #     return user


class ActivateForm(forms.Form):
    code = forms.CharField(label='код активации')
    username = forms.CharField(label='имя пользователя')
