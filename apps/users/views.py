from django.contrib.auth import get_user_model, login
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, UpdateView, DeleteView

from apps.users.forms import UserRegisterForm

User = get_user_model()


def index(request: WSGIRequest):
    return render(
        request=request,
        template_name="index.html",
    )


class RegisterFormView(FormView):
    form_class = UserRegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("contacts:root")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("contacts:root")


class UserDetailView(DetailView):
    model = User
    template_name = "users/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Details User"
        return context


class UserUpdateView(UpdateView):
    model = User
    template_name = "users/update.html"
    fields = ("username", "email", "first_name", "last_name", "avatar")
    success_url = reverse_lazy("contacts:root")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Details User"
        return context


class UserDeleteView(DeleteView):
    model = User

    success_url = reverse_lazy("contacts:root")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Account"
        return context
