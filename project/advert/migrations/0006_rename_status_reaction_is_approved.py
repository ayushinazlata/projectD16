# Generated by Django 4.2.4 on 2023-08-20 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0005_rename_user_reaction_author_reaction_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reaction',
            old_name='status',
            new_name='is_approved',
        ),
    ]
