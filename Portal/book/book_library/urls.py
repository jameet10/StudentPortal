from django.urls import path
from book_library import views
from django.contrib import admin

urlpatterns = [
    path("", views.index, name="book_library"),   
    path("library_availibility/", views.library_availibility, name="library_availibility"), 
    path("book_issue", views.book_issue, name="book_issue"),
    path("solved_p", views.solved_p, name="solved_p"),
    path("lib_e", views.lib_e, name="lib_e"),
    

]
