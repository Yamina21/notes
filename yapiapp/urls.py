from django.urls import path, include
# from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet


router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename="note")
urlpatterns = [
    # path('', views.note_list, name='note_list'),
    # path('add/', views.add_note, name='add_note'),
    # path('edit/<int:pk>/', views.edit_note, name='edit_note'),
    # path('delete/<int:pk>/', views.delete_note, name='delete_note'),
    # path('register/', views.register_view, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('api/notes/', NoteList.as_view(), name='note_list_api'),
    # path('api/notes/<int:pk>/', NoteDetail.as_view(), name='note_detail_api'),
    path('', include(router.urls)),



    
]
