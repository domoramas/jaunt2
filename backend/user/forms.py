from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CreateUserForm(UserCreationForm):

  class Meta:
    model = CustomUser
    fields = ('email','first_name', 'last_name', 'email','city', 'state')

class ChangeUserForm(UserChangeForm):


  class Meta:
    model = CustomUser
    fields = ('email','first_name', 'last_name', 'email','city', 'state')