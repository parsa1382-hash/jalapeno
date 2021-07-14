from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
	path('', views.login, name='login'),
	path('welcome/', views.welcome, name='welcome'),
	path('room/<int:room_id>', views.room, name='room'),
]