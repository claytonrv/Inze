import pytest

from django.contrib.auth.models import User

@pytest.fixture
@pytest.mark.django_db
def user():
    return User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

@pytest.fixture
def csv_filename():
    return "nubank-2015-08.csv"