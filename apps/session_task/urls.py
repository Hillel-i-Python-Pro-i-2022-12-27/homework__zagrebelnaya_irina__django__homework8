from django.urls import path

from . import views

app_name = "session_task"

urlpatterns = [
    path("", views.SessionTaskView.as_view(), name="index"),
]
