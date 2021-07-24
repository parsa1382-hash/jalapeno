from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'spreedsheet'

urlpatterns = [
	path('', views.home, name='home'),
	path('sheet/<str:group>', views.spreedsheet, name='spreedsheet'),
	path('task/<int:num>/<str:group>', views.task, name='task'),
	path('change_status/<str:group>/<int:id>/<int:status>', views.change_status, name='change_status'),
]