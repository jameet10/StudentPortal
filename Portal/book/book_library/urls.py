from django.urls import path
from book_library import views
from django.contrib import admin
from . import views

admin.site.site_header = "Library Admin"
admin.site.site_title = "Srmcem Library Admin Portal"
admin.site.index_title = "Welcome to Library "

urlpatterns = [
    path("", views.index, name="book_library"),   
    path("library_availibility/", views.library_availibility, name="library_availibility"), 
    path("book_issue", views.book_issue, name="book_issue"),
    path("solved_p", views.solved_p, name="solved_p"),
<<<<<<< HEAD
    path("lib_e", views.save_lib_e, name="lib_e"),
=======
    path("lib_e", views.save_lib_e, name="save_lib_e"),
>>>>>>> 74cad7ea9c98a86a45e7f8819c842cc09b57bcd7
    path('search_pyqs', views.search_pyqs, name='search_pyqs'),
    

]



