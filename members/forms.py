
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30,
                               widget=forms.TextInput(attrs={
                                   'name': 'username',
                                   'placeholder': 'Username',
                                   'required': True,
                                   'autofocus': True,
                                   'class': 'form-control'}))

    password = forms.CharField(label='Password', max_length=30,
                               widget=forms.PasswordInput(attrs={
                                   'name': 'password',
                                   'placeholder': 'Password',
                                   'class': 'form-control'}))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=30,
                               widget=forms.TextInput(attrs={
                                   'name': 'username',
                                   'placeholder': 'Account',
                                   'required': True,
                                   'autofocus': True,
                                   'class': 'form-control'}))

    first_name = forms.CharField(label='First Name', max_length=30,
                                 widget=forms.TextInput(attrs={
                                     'name': 'first_name',
                                     'placeholder': 'First Name',
                                     'class': 'form-control'}))

    last_name = forms.CharField(label='Last Name', max_length=30,
                                widget=forms.TextInput(attrs={
                                    'name': 'last_name',
                                    'placeholder': 'Last Name',
                                    'class': 'form-control'}))

    email = forms.EmailField(label='Email', max_length=254,
                             widget=forms.TextInput(attrs={
                                 'name': 'email',
                                 'placeholder': 'Email',
                                 'class': 'form-control'}))

    password1 = forms.CharField(label='Password', max_length=30,
                                widget=forms.PasswordInput(attrs={
                                    'name': 'password1',
                                    'placeholder': 'Password',
                                    'class': 'form-control'}))

    password2 = forms.CharField(label='Password', max_length=30,
                                widget=forms.PasswordInput(attrs={
                                    'name': 'password2',
                                    'placeholder': 'Confirm Password',
                                    'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user
