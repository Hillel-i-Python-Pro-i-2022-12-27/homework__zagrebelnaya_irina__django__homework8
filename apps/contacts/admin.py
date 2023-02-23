# Register your models here.
from django.contrib import admin

from . import models


@admin.register(models.Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "created_at",
        "modified_at",
    )
    list_filter = (
        "name",
        "phone",
        "created_at",
    )


class ContactsInline(admin.TabularInline):
    model = models.Contact


@admin.register(models.Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
        "modified_at",
    )
    inlines = (ContactsInline,)
