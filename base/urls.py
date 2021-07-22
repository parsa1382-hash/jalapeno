from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
	path('', views.home, name='home'),
	path('login/', views.login_view, name='login_view'),
	path('check/', views.check, name='check'),
	path('room/<int:room_id>', views.room, name='room'),
	path('change_release/<int:room_id>', views.change_release, name='change_release'),
]