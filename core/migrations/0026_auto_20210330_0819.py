# Generated by Django 3.0.6 on 2021-03-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20210329_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersid',
            name='players_name_given',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
