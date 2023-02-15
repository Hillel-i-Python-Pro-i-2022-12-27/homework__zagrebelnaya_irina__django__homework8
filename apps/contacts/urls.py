from django.urls import path

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path('', views.list_of_contacts),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path("info/", views.info, name="info"),
    path("delete/", views.delete, name="delete"),
]
