from django.views.generic import DetailView, CreateView, TemplateView
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm

# Create your views here.

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'members/profile.html'

    def get_object(self, *args, **kwargs):
        current_user = self.request.user
        user = super(ProfileView, self).get_object(*args, **kwargs)

        if current_user.is_superuser or \
            current_user.is_staff or current_user == user:
            return user
        raise PermissionDenied


class RegistrationView(CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'members/registration.html'

    def get_success_url(self):
        return reverse('members:success')


class SuccessMessageView(TemplateView):
    template_name = 'members/registration_success.html'        
    
