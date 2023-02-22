from django.core.exceptions import ValidationError
from django.db import models
from django.forms import ModelForm


class Provider(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    __repr__ = __str__


class Contacts(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=13, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name="contacts",
        default=None,
        null=True,
        blank=False,
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"

    __repr__ = __str__


class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'phone', 'provider']


