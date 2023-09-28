from rest_framework import mixins, viewsets


class ListRetrieveUpdateDestroyViewSet(mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin,
                                       mixins.ListModelMixin,
                                       viewsets.GenericViewSet):
    """Вьюсет для просмотра, обновления и удаления."""
