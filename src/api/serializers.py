from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.validators import validate_password

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор создания пользователей."""

    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())], required=False)

    def validate_password(self, value):
        return validate_password(value, User)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password',)
        extra_kwargs = {'password': {'write_only': True}}


class UserEditSerializer(serializers.ModelSerializer):
    """Сериализатор изменения пользователей."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'dob', 'gender')
        read_only_fields = ('id', 'username',)


class IdResponseSerializer(serializers.Serializer):
    """Сериализатор ответа после создания чего-либо."""

    id = serializers.IntegerField(min_value=1)