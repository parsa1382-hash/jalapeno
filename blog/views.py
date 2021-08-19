from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from spreedsheet.models import Task

def utc(request):
	user_tasks = Task.objects.filter(user=request.user)
	ut = 0
	for i in user_tasks:
		ut += 1
	return ut


def blog(request):
	if request.user.is_authenticated:
		posts = Post.objects.filter(status=1).order_by('-created_on')

		if not posts:
			posts = False

		return render(request, 'blog/blog.html', context={'posts': posts, 'ut': utc(request),})
	else:
		return redirect('base:login_view')

def post_detail(request, slug):
	if request.user.is_authenticated:
		post = get_object_or_404(Post, slug=slug)
		return render(request, 'blog/post_detail.html', context = {'post': post, 'ut': utc(request),})
	else:
		return redirect('base:login_view')



# Create your views here.
