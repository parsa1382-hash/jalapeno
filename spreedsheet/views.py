from django.shortcuts import render, HttpResponse
from .models import Task

def spreedsheet(request):
	tasks = Task.objects.order_by('-updated_on')

	todo = Task.objects.filter(status=0).order_by('-updated_on')
	in_progress = Task.objects.filter(status=1).order_by('-updated_on')
	done = Task.objects.filter(status=2).order_by('-updated_on')

	context = {'tasks': tasks, 'todo': todo, 'in_progress': in_progress, 'done': done}
	return render(request, 'spreedsheet/spreedsheet.html', context)
# Create your views here.
