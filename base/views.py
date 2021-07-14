from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Room

users = [
{'username': 'p.amini', 'password': '1234', 'room1': True, 'room2': True, 'room3': True},
{'username': 'a.radani', 'password': '1234', 'room1': True, 'room2': True, 'room3': True},
{'username': 'm.mokaram', 'password': '1234', 'room1': True, 'room2': True, 'room3': True},
]

check = []
for user in users:
	check.append({'username': user.get('username'), 'password': user.get('password')})

def login(request):
	return render(request, 'base/login.html')

def welcome(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)

		if user is not None:
			rooms = Room.objects.all()
			

			allowed_room = []
			for room in rooms:
				if room.release:
					for us in room.users.all():
						print(type(get_object_or_404(User, pk=us.id)))

						if str(get_object_or_404(User, pk=us.id)) == user.username:
							allowed_room.append(room)
			if allowed_room == []:
				allowed_room = "not_allowed"

			context = {
				'rooms': allowed_room,
				'user': user,
			}
			return render(request, 'base/base.html', context)

		else:
			return redirect('base:login')
	else:
		return render(request, 'base/login.html')

def room(request, room_id):
	room = get_object_or_404(Room, pk=room_id)
	return render(request, 'base/room.html', {'room': room})


def room1(request):
	return render(request, 'base/room1.html')
def room2(request):
	return render(request, 'base/room2.html')
def room3(request):
	if request.user.is_authenticated:
		return render(request, 'base/room3.html')
	else:
		return HttpResponse("NO")
# Create your views here.
