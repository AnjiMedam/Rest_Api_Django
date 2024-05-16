from django.urls import path
from . import views
urlpatterns = [
    path("", views.Booklist,name='booklist' ),
    path("add/",views.Post_Book,name='post_book'),
    path("update/<int:id>/",views.Update_Book,name='update_Book'),
    path("delete/<int:id>/",views.Delete_Book,name='delete_Book'),
]

