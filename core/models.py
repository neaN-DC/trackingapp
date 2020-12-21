from django.db import models

# Create your models here.

class UsersIds(models.Model):
	playersNameGive = models.CharField(max_length=50, unique=True)
	player_id = models.CharField(max_length=50, unique=True)
	
	def __str__(self):
		return  self.player_id

class SteamId(models.Model):
	playersteam_id = models.CharField(max_length=50, unique=True)
	def __str__(self):
		return  self.playersteam_id




