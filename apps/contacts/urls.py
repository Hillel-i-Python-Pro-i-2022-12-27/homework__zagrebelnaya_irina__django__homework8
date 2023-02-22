from django.urls import path

from apps.contacts import views

app_name = "contacts"

urlpatterns = [


    path("", views.list_of_contacts, name="root"),
    path("list/",  views.list_of_contacts, name='list'),

    path('create/', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path("info/<int:pk>", views.info, name="info"),
    path("delete/", views.delete, name="delete"),
]
