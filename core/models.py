from django.db import models

# Create your models here.

class Post(models.Model):
	player_id = models.CharField(max_length=50)
	def __str__(self):
		return self.player_id
