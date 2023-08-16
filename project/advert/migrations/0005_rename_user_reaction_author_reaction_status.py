# Generated by Django 4.2.4 on 2023-08-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0004_remove_post_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reaction',
            old_name='user',
            new_name='author',
        ),
        migrations.AddField(
            model_name='reaction',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]