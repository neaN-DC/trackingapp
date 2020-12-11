from django.db import models

# Create your models here.

class UsersIds(models.Model):
	player_id = models.CharField(max_length=50, unique=True)
	name = models.CharField(max_length=50, unique=True)
	def __str__(self):
		return self.player_id
