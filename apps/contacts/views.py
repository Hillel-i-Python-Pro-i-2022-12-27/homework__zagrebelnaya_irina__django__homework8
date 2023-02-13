from django.shortcuts import render, redirect

from apps.contacts.models import ContactForm
from apps.contacts.models import Contacts


def list_of_contacts(request):
    queryset = Contacts.objects.all()
    contacts_dict = {
        'contacts': queryset
    }
    return render(request, 'contacts/list.html', contacts_dict)


def create(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:

        form = ContactForm()

        return render(request, 'contacts/create.html', {'form': form})


def edit(request, pk):
    obj = Contacts.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = ContactForm(instance=obj)

    return render(request,
                  'contacts/edit.html',
                  {'form': form})


def info(request):
    uuid = int(request.POST.get('uuid'))
    queryset = Contacts.objects.get(id=uuid)
    contacts_dict = {
        'contacts': queryset
    }
    return render(request, 'contacts/info.html', contacts_dict)


def delete(request):
    uuid = int(request.POST.get('uuid'))
    item = Contacts.objects.get(id=uuid)
    item.delete()

    return redirect('/')
