# Generated by Django 3.0.6 on 2020-12-20 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20201216_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='SteamId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playersteam_id', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]