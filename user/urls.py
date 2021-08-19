from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'user'

urlpatterns = [
	path('', views.profile, name='profile'),
	path('check/', views.check, name='check'),
	path('login/', views.login_view, name='login_view'),
]