# Generated by Django 3.0.6 on 2020-12-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20201221_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersids',
            name='playersteam_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]