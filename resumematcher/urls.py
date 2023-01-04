from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_posting, name="home"),
]
