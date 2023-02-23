from django.contrib import messages
from django.core.checks import CRITICAL
from django.shortcuts import render, redirect

from apps.contacts.forms import ContactForm
from apps.contacts.models import Contact


def list_of_contacts(request):
    queryset = Contact.objects.all()
    contacts_dict = {"contacts": queryset}
    return render(request, "contacts/list.html", contacts_dict)


def create(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if not (request.POST.get("name").isalpha()):
            messages.add_message(request, CRITICAL, "Name must have only letters.")
            return redirect("contacts:create_contact")
        if not (request.POST.get("phone").isdigit()):
            messages.add_message(request, CRITICAL, "Phone must have only numbers.")
            return redirect("contacts:create_contact")
        if form.is_valid():
            form.save()
            return redirect("contacts:list_contact")
    else:
        form = ContactForm()

        return render(request, "contacts/form.html", {"form": form})


def edit(request, pk):
    obj = Contact.objects.get(pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("contacts:list_contact")
        else:
            form = ContactForm(instance=obj)

    return render(request, "contacts/form.html", {"form": form})


def info(request, pk):
    queryset = Contact.objects.get(id=pk)
    contacts_dict = {"contacts": queryset}
    return render(request, "contacts/info.html", contacts_dict)


def delete(request):
    uuid = int(request.POST.get("uuid"))
    item = Contact.objects.get(id=uuid)
    item.delete()

    return redirect("contacts:list_contact")
