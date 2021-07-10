from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

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


		if {'username': username, 'password': password} in check:
			messages.add_message(request, messages.INFO, 'login successful')
			user = [i for i in users if i["username"]==username]
			print(user)
			context = user[0]
			return render(request, 'base/base.html', context)

		else:
			return redirect('base:login')
	else:
		return render(request, 'base/login.html')


def test(request):
	return render(request, 'base/test.html')
# Create your views here.
