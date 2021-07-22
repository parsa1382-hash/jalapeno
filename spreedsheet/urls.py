from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'spreedsheet'

urlpatterns = [
	path('', views.spreedsheet, name='spreedsheet'),
]