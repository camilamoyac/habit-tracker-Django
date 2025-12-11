from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_habit, name='add_habit'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='habits/login.html'), name='login'),
]
