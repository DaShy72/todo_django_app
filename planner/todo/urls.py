from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('task_list/', views.task_list, name='task_list'),
    path('new/', views.task_create, name='task_create'),
    path('register/', views.register, name='register'),
    path('edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('welcome/', views.welcome, name='welcome'),
    path('goodbye/', views.goodbye, name='goodbye'),
]