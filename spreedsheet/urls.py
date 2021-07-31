from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'spreedsheet'

urlpatterns = [
	path('', views.home, name='home'),
	path('sheet/<str:group>', views.spreedsheet, name='spreedsheet'),
	path('task/<int:num>/<str:group>', views.task, name='task'),
	path('task_status/<str:group>/<int:id>/<int:status>', views.task_status, name='task_status'),
	path('task_delete/<str:group>/<int:id>', views.task_delete, name='task_delete'),
	path('task_edit/<str:group>/<int:task_id>', views.task_edit, name='task_edit'),
	path('task_edit_html/<str:group>/<int:task_id>/<str:task_form_id>', views.task_edit_html, name='task_edit_html'),
]