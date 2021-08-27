from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from spreedsheet.models import Task

def login_view(request):
	return render(request, 'user/login.html')

def profile(request):
	if request.user.is_authenticated:

		tasks = Task.objects.filter(user=request.user)
		len_tasks = len(tasks)
		context = {
			'tasks': tasks,
			'len_tasks': len_tasks,
		}
		return render(request, 'user/profile.html', context)
	else:
		return redirect('user:login_view')

def check(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('user:profile')
		else:
			messages.add_message(request, messages.INFO, 'Bad Username/Password')
			return redirect('user:login_view')