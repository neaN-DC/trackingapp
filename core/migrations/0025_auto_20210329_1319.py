# Generated by Django 3.0.6 on 2021-03-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20201222_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersid',
            name='players_name_given',
            field=models.CharField(max_length=50),
        ),
    ]