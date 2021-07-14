from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
	path('', views.login, name='login'),
	path('welcome/', views.welcome, name='welcome'),
	path('room1', views.room1, name='room1'),
	path('room2', views.room2, name='room2'),
	path('room3', views.room3, name='room3'),
]