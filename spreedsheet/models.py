from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from base.models import Group
from django.shortcuts import get_object_or_404


STATUS = (
    (0,"todo"),
    (1,"inprogress"),
    (2,"done")
)

class Task(models.Model):
	content = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'task')
	status = models.IntegerField(choices=STATUS, default=0)
	updated_on = models.DateTimeField(auto_now = True)

	creator = models.ForeignKey(User ,null = True, on_delete = models.CASCADE, related_name = 'creator')
	group = models.ForeignKey(Group ,null = True,  on_delete = models.CASCADE)
	def __str__(self):
		return self.content
		