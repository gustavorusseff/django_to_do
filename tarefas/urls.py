from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.task_list_create, name='lista'),
    path('<int:pk>/toggle/', views.toggle_done, name='toggle'),
]