from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):

  # setting email as username

  def create_user(self, email, password, first_name, last_name, city, state):
    if not email:
      raise ValueError(_('The Email must be set'))
    email = self.normalize_email(email)
    user = self.model(email = email, first_name = first_name, last_name = last_name, city = city, state = state)
    user.set_password(password)
    user.save()
    return user