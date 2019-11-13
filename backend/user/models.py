from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _ 

from .managers import CustomUserManager

# creating customuser 

class CustomUser(AbstractUser):
  pass
  username = None
  email = models.EmailField(_('email address'), unique=True)
  city = models.CharField(max_length=20, null = True, blank = True)
  state = models.CharField(max_length=20, null = True, blank = True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  def __str__(self):
    return self.email
  
