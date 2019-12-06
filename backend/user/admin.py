from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import ChangeUserForm, CreateUserForm

# Register your models here.
# admin.site.unregister(User)

# @admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
  add_form = CreateUserForm
  form = ChangeUserForm
  model = CustomUser
  ordering = ('email',)



admin.site.register(CustomUser, CustomUserAdmin)