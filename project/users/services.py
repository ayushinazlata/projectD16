import random
import string

from django.core.mail import EmailMultiAlternatives


def generate_random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(6))


def send_message(username, email, title, message):
    subject = 'Добро пожаловать на наш портал объявлений!'
    text = f'{username}, {title}'

    html = (
        f'<b>{username}</b>, {message}'
    )
    msg = EmailMultiAlternatives(
        subject=subject, body=text, from_email=None, to=[email]
    )
    msg.attach_alternative(html, "text/html")
    msg.send()
