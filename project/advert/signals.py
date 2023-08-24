from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from advert.models import Reaction


@receiver(post_save, sender=Reaction)
def reaction_created(instance, created, **kwargs):
    if created:
        send_mail(
            subject='На ваше объявление откликнулись!',
            message=f'{instance.post.author.username}, пользователь {instance.author} оставил отклик на ваше '
                    f'объявление! Вот он: "{instance.text}"',
            from_email=None,
            recipient_list=[instance.post.author.email],
        )

