from django.contrib.auth import get_user_model

from django_filters import rest_framework as filters

User = get_user_model()


class UserFilter(filters.FilterSet):
    """Фильтр пользователей."""

    gender = filters.NumberFilter()
    username = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    email = filters.CharFilter(lookup_expr='icontains')
    pub_date = filters.DateRangeFilter()

    class Meta:
        fields = ('username', 'last_name', 'email', 'gender', 'pub_date')
        model = User
