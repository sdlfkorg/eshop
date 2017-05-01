from .forms import RegistrationForm
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView, TemplateView

# from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash


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


def change_password(request):
    template_response = views.password_change(request)
    print(template_response)
    # Do something with `template_response`
    return template_response


# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('accounts:change_password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'accounts/change_password.html', {
#         'form': form
#     })
    
