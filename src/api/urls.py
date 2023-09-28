from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register('users', views.UserViewSet, 'users')


urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='api-create-user'),
    path('v1/', include(router.urls)),
]
