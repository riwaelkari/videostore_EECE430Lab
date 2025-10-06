from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_videos, name='list_videos'),
    path('add/', views.add_video, name='add_video'),
    path('edit/<int:pk>/', views.edit_video, name='edit_video'),
    path('delete/<int:pk>/', views.delete_video, name='delete_video'),
]
