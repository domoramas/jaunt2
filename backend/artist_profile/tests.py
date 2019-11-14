from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

# Create artist profile model and form then post to db

class artist_profile_creation_tests(TestCase):

  def artist(self):
    artist = get_user_model()