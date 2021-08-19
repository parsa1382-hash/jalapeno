from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Room, Group
from spreedsheet.models import Task
from datetime import timedelta

def utc(request):
	user_tasks = Task.objects.filter(user=request.user)
	ut = 0
	for i in user_tasks:
		ut += 1
	return ut

def login_view(request):
	return render(request, 'base/login.html')

def check(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('base:home')
		else:
			messages.add_message(request, messages.INFO, 'Bad Username/Password')
			return redirect('base:login_view')


def home(request):
	if request.user.is_authenticated:

		rooms = Room.objects.all()
		allowed_room = []
		user = request.user

		for room in rooms:
			if user.is_superuser:
				allowed_room.append(room)

			else:
				if room.release:
					for us in room.users.all():

						if str(get_object_or_404(User, pk=us.id)) == user.username:
							allowed_room.append(room)

					for group in room.groups.all():
						for us in group.members.all():

							if str(get_object_or_404(User, pk=us.id)) == user.username:
								if room in allowed_room:
									pass

								else:
									allowed_room.append(room)

		if allowed_room == []:
			allowed_room = "not_allowed"


		context = {
			'rooms': allowed_room,
			'user':user,
			'ut': utc(request),
		}
		return render(request, 'base/base.html', context)
	else:
		return redirect('base:login_view')



def room(request, room_id):
	if request.user.is_authenticated:
		room = get_object_or_404(Room, pk=room_id)
		return render(request, 'base/room.html', {'room': room, 'ut': utc(request),})
	else:
		return render(request, 'base/login.html')

def change_release(request, room_id):
	if request.user.is_authenticated:
		room = get_object_or_404(Room, pk=room_id)

		if room.release:
			room.release = False
			room.save()

		else:
			room.release = True
			room.save()

		return redirect('base:home')
	else:

		return render(request, 'base/login.html')


# Create your views here.
