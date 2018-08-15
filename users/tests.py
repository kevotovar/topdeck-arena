from django.test import TestCase

from .models import User

# Create your tests here.
class UserModelTest(TestCase):

    def test_string_representation(self):
        user = User(email="kevin@gmail.com")
        self.assertEqual(str(user), user.email)
