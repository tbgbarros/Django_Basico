from django.urls import path
from . import views


urlpatterns = [
    path("", views.natal),
    path("independencia", views.independencia),
    path("tiradentes", views.tiradentes),
    path("natal", views.natal),
]
