from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='NULL', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

			

class UserslistId(models.Model):
	auto_increment_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	players_name_given = models.CharField(max_length=50, unique=True)
	player_id = models.CharField(max_length=50,unique=True)
	playersteam_id = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.players_name_given