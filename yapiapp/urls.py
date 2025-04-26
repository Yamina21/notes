from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('add/', views.add_note, name='add_note'),
    path('edit/<int:pk>/', views.edit_note, name='edit_note'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
