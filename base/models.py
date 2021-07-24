from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Group(models.Model):
	name = models.CharField(max_length=200)
	members = models.ManyToManyField(User)

	def __str__(self):
		return self.name

class Room(models.Model):
	name = models.CharField(max_length=300)
	
	url = models.URLField(max_length=500)
	release = models.BooleanField(default = True)

	users = models.ManyToManyField(User, default = None)
	groups = models.ManyToManyField(Group, default = None)

	def __str__(self):
		return self.name
# Create your models here.
