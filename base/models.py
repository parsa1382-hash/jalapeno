from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
	name = models.CharField(max_length=300)
	url = models.URLField(max_length=500)
	users = models.ManyToManyField(User)
	release = models.BooleanField(default = True)


	def __str__(self):
		return self.name
# Create your models here.
