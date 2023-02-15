from django.urls import path, include


urlpatterns = [
    path("", include("apps.contacts.urls_root")),
]
