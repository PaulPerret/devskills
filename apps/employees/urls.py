from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("find", views.find_an_expert, name="find_an_expert")
]