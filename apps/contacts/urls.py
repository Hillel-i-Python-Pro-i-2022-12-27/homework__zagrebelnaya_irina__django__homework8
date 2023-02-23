from django.urls import path

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("", views.list_of_contacts, name="root"),
    path("list/", views.list_of_contacts, name="list_contact"),
    path("create/", views.create, name="create_contact"),
    path("edit/<int:pk>", views.edit, name="edit_contact"),
    path("info/<int:pk>", views.info, name="info_contact"),
    path("delete/", views.delete, name="delete_contact"),
]
