from django.urls import path
from . import views

urlpatterns = [
    path("api_home/", views.api_home, name="api_home"),
]
