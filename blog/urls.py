from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
	path('', views.blog, name='blog'),
	path('post_detail/<slug:slug>/', views.post_detail, name='post_detail'),
]