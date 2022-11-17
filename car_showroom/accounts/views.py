from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views import generic as views

from car_showroom.accounts.forms import SignUpForm


def index(request):
    pass


class SignUpView(views.CreateView):
    template_name = 'accounts/register-view.html'
    form_class = SignUpForm


class SignInView(auth_views.LoginView):
    pass


class SignOutView(auth_views.LogoutView):
    pass


class UserDetailView(views.DetailView):
    pass


class UserEditView(views.UpdateView):
    pass


class UserDeleteView(views.DeleteView):
    pass
