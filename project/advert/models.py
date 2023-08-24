from django.db import models
from users.models import User
from tinymce import models as tinymce_models


class Category(models.Model):
    name = models.CharField('название', max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Post(models.Model):
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    category = models.ForeignKey(
        Category,
        related_name='posts',
        verbose_name='категория',
        on_delete=models.CASCADE,
    )
    title = models.CharField('заголовок', max_length=256)
    attachments = tinymce_models.HTMLField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
        related_name='posts'
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'

    def get_absolute_url(self):
        return f'/adverts/{self.id}'


class Reaction(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='отклик',
        related_name='reactions',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
        related_name='reactions',
    )
    text = models.TextField('текст')
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.post}'

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'отклик'
        verbose_name_plural = 'отклики'
