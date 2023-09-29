import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_create_user(user_client):
    url = reverse('api-create-user')
    data = {
        'username': 'test_user1',
        'password': 'test_password',
        'email': 'test@aaaaa.com',
        'first_name': 'Test',
        'last_name': 'User',
    }
    response = user_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in response.data


@pytest.mark.django_db
def test_create_user_invalid_data(user_client):
    url = reverse('api-create-user')
    data = {
        'username': 'test_user',
        'password': 'short',
    }
    response = user_client.post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_get_user(user_client, user):
    url = reverse('users-detail', args=[user.id])
    response = user_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['username'] == 'test_user'


@pytest.mark.django_db
def test_get_user_not_found(user_client):
    url = reverse('users-detail', args=[999])
    response = user_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_update_user(user_client, user, admin_client):
    url = reverse('users-detail', args=[user.id])
    data = {'first_name': 'Updated'}
    response = user_client.patch(url, data)
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = admin_client.patch(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['first_name'] == 'Updated'
    user.refresh_from_db()
    assert user.first_name == 'Updated'


@pytest.mark.django_db
def test_update_user_invalid_data(admin_client, user):
    url = reverse('users-detail', args=[user.id])
    data = {'email': 'invalid_email'}
    response = admin_client.patch(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_delete_user(user_client, user, admin_client):
    url = reverse('users-detail', args=[user.id])
    response = user_client.delete(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = admin_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    user.refresh_from_db()
    assert user.deleted is True


@pytest.mark.django_db
def test_delete_user_not_found(user_client):
    url = reverse('users-detail', args=[999])
    response = user_client.delete(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
