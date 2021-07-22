from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def blog(request):
	if request.user.is_authenticated:
		posts = Post.objects.filter(status=1).order_by('-created_on')

		if not posts:
			posts = False

		return render(request, 'blog/blog.html', context={'posts': posts})
	else:
		return redirect('base:login_view')

def post_detail(request, slug):
	if request.user.is_authenticated:
		post = get_object_or_404(Post, slug=slug)
		return render(request, 'blog/post_detail.html', context = {'post': post})
	else:
		return redirect('base:login_view')



# Create your views here.
