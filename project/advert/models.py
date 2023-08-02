from django.db import models
from django.contrib.auth.models import User
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
    TANK = 'TN'
    HEALER = 'HL'
    DAMAGE_D = 'DD'
    TRADER = 'TR'
    GOLD_MASTER = 'GM'
    QUEST_GIVER = 'QG'
    BLACKSMITH = 'BS'
    TANNER = 'TA'
    POTION_MASTER = 'PM'
    SPELL_MASTER = 'SM'

    CATEGORIES = (
        (TANK, 'Танки'),
        (HEALER, 'Хилы'),
        (DAMAGE_D, 'ДД'),
        (TRADER, 'Торговцы'),
        (GOLD_MASTER, 'Голдмастеры'),
        (QUEST_GIVER, 'Квестгиверы'),
        (BLACKSMITH, 'Кузнецы'),
        (TANNER, 'Кожевники'),
        (POTION_MASTER, 'Зельевары'),
        (SPELL_MASTER, 'Мастера заклинаний'),
    )

    publication = models.CharField(max_length=2, choices=CATEGORIES, default=TANK)
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    category = models.ManyToManyField(
        Category,
        through='PostCategory',
        verbose_name='категория',
    )
    title = models.CharField('заголовок', max_length=256)
    text = models.TextField('текст')
    attachments = tinymce_models.HTMLField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
        related_name='posts'
    )

    @property
    def preview(self):
        if len(self.text) > 128:
            return f'{self.text[0:128]}...'
        return f'{self.text}'

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'

    # def get_absolute_url(self):
    #     return f'/adverts/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='объявление',
        related_name='post_category',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='категория',
        related_name='post_category',
    )

    def __str__(self):
        return f'объявление {self.post} категория {self.category}'

    class Meta:
        verbose_name = 'объявление по категории'
        verbose_name_plural = 'объявления по категориям'


class Reaction(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='отклик',
        related_name='reactions',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
        related_name='reactions',
    )
    text = models.TextField('текст')
    created_at = models.DateTimeField('дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.post}'
