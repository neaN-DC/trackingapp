# Generated by Django 3.0.6 on 2020-12-21 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_steamid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UsersIds',
            new_name='UsersIdss',
        ),
        migrations.RenameField(
            model_name='usersidss',
            old_name='player_name',
            new_name='playersNameGive',
        ),
    ]