from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Room, Group




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
				'user': user,
			}
			return render(request, 'base/base.html', context)

		else:
			return redirect('base:login')
	else:
		return render(request, 'base/login.html')


def room(request, room_id):
	if request.user.is_authenticated:
		room = get_object_or_404(Room, pk=room_id)
		return render(request, 'base/room.html', {'room': room})
	else:
		return render(request, 'base/login.html')

# Create your views here.
