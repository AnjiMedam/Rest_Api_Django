
from django.urls import path
from .import views
urlpatterns = [
   
   path('', views.Movielist, name='movielist'),
    path('adding/', views.Post_movie, name='post_movie'),
    path('update/<int:id>/', views.Update_movie, name='update_movie'),
    path('delete/<int:id>/', views.Delete_movie, name='delete_movie'),
]




