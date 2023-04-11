from django.urls import path

from . import views

app_name = "logs"

urlpatterns = [
    path("", views.RequestsLogsListView.as_view(), name="list"),
    path("session_id", views.RequestsLogsListViewForSession.as_view(), name="list_for_session"),
    path("<int:username>", views.RequestsLogsListViewForUser.as_view(), name="list_for_user"),
]
