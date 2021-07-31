from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Task
from base.models import Group
from django.utils import timezone


def spreedsheet(request, group):
	if request.user.is_authenticated:
		tasks = Task.objects.order_by('-updated_on').filter(group=group)

		todo = tasks.filter(status=0)
		in_progress = tasks.filter(status=1)
		done = tasks.filter(status=2)

		context = {
			'tasks': tasks, 
			'todo': todo, 
			'in_progress': in_progress, 
			'done': done, 'group': group, 
			'gr': get_object_or_404(Group, id=group)
			}
		return render(request, 'spreedsheet/spreedsheet.html', context)
	else:
		return redirect('base:login_view')


def home(request):
	if request.user.is_authenticated:
		context = {
			'groups': Group.objects.filter(members = request.user).order_by('-name')
		}

		return render(request, 'spreedsheet/home.html', context)
	else:
		return redirect('base:login_view')


def task(request, num, group):
	if request.user.is_authenticated:
		content = username = request.POST['textarea']
		print(group)

		t = Task(content=content, updated_on=timezone.now(), group=get_object_or_404(Group, id=group), user=request.user, status=num)
		t.save()

		return	redirect('spreedsheet:spreedsheet', group)
	else:
		return redirect('base:login_view')

def task_delete(request, group, id):
	if request.user.is_authenticated:
		t = get_object_or_404(Task, id=id)
		t.delete()

		return redirect('spreedsheet:spreedsheet', group)
	else:
		return redirect('base:login_view')

def task_status(request, group, id, status):
	if request.user.is_authenticated:
		t = get_object_or_404(Task, id=id)
		t.status = status
		t.updated_on = timezone.now()

		t.save()

		return	redirect('spreedsheet:spreedsheet', group)
	else:
		return redirect('base:login_view')

def task_edit(request, group, task_id):
	if request.user.is_authenticated:
		t = get_object_or_404(Task, id=task_id)
		t.content = request.POST['textarea']

		t.save()

		return	redirect('spreedsheet:spreedsheet', group)
	else:
		return redirect('base:login_view')

def task_edit_html(request, group, task_id, task_form_id):
	if request.user.is_authenticated:
		context = {'task_id': task_id, 
			'group': group, 
			'task':get_object_or_404(Task, id=task_id),
			'task_form_id': task_form_id,
			}

		return render(request, 'spreedsheet/edit.html', context)
		#this function make for ajax and load with js on frontend
	else:
		return redirect('base:login_view')
