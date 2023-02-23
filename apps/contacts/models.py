from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    __repr__ = __str__


class Contact(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=13, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(
        max_length=255,
        upload_to="contacts/contact/avatar/",
        blank=True,
        null=True,
    )

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
