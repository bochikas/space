from django.contrib.auth import get_user_model

import pytest
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


@pytest.fixture
def admin():
    return User.objects.create(username='admin', email='admin@fake.fake', password='1234567', is_staff=True)


@pytest.fixture
def user():
    return User.objects.create(username='test_user', email='test@fake.fake', password='1234567')


@pytest.fixture
def user_token(user):
    refresh = RefreshToken.for_user(user)

    return str(refresh.access_token)


@pytest.fixture
def admin_token(admin):
    refresh = RefreshToken.for_user(admin)

    return str(refresh.access_token)


@pytest.fixture
def user_client(user_token):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {user_token}')
    return client


@pytest.fixture
def admin_client(admin_token):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {admin_token}')
    return client
