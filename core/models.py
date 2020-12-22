from django.db import models

# Create your models here.

class UsersId(models.Model):
	players_name_given = models.CharField(max_length=50, unique=True)
	player_id = models.CharField(max_length=50, unique=True)
	playersteam_id = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.players_name_given
	




