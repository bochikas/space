from django.contrib.auth import get_user_model

from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse
from rest_framework import response, status, views

from api.filters import UserFilter
from api.mixins import ListRetrieveUpdateDestroyViewSet
from api.permissions import IsAuthenticatedAndAdminOrReadOnlyPermission
from api.serializers import IdResponseSerializer, UserSerializer, UserEditSerializer
from api.services import create_user, update_user, soft_delete_user

User = get_user_model()


class CreateUserView(views.APIView):
    """Регистрация пользователей."""

    @extend_schema(request=UserSerializer,
                   responses={201: OpenApiResponse(response=IdResponseSerializer,
                                                   description='Created. Id in response'),
                              400: OpenApiResponse(description='Bad request')})
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user(**serializer.validated_data)
        return response.Response({'id': user.id}, status=status.HTTP_201_CREATED)


@extend_schema_view(
    retrieve=extend_schema(description='Получение информации по определенному пользователю.'),
    list=extend_schema(description='Список всех активных пользователей.'),
    partial_update=extend_schema(description='Обновление данных пользователя.'),
    destroy=extend_schema(description='Удаление пользователя.'),
)
class UserViewSet(ListRetrieveUpdateDestroyViewSet):
    """Вьюсет пользователей."""

    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedAndAdminOrReadOnlyPermission]
    filterset_class = UserFilter
    http_method_names = ['get', 'patch', 'delete']

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return UserEditSerializer
        return UserSerializer

    def perform_destroy(self, instance):
        soft_delete_user(instance)

    def perform_update(self, serializer):
        update_user(user=serializer.instance, **serializer.validated_data)
