# Generated by Django 3.0.6 on 2020-12-22 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20201222_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersid',
            old_name='player_name_given',
            new_name='players_name_given',
        ),
    ]
