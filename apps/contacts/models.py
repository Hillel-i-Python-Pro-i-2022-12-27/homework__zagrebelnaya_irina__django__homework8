from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.db import models
from django.forms import ModelForm


class Contacts(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=13, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"

    __repr__ = __str__


class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'phone']

    # def clean(self):
    #     if not self.phone.isdigit():
    #         raise ValidationError(
    #             "Phone must have only numbers!"
    #         )
    #     if not self.name.isalpha():
    #         raise ValidationError(
    #             "Name must have only letters!"
    #         )
