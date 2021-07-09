# this is app urls

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Signin/", views.Singin, name="Signin"),
    path("Login/", views.Login, name="Login"),
    path("About/", views.About, name="About"),
    path("Create/", views.Create, name="Create"),
    path("update/<int:pk>/<int:n>", views.Update, name="Update"),
    path("delete/<int:pk>/<int:n>", views.Delete, name="Delete"),
    path("Logout/", views.Logout, name="Logout")
]