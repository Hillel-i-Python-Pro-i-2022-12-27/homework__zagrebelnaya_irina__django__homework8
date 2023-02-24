from django.forms import ModelForm

from apps.contacts.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["avatar", "name", "phone", "provider"]
