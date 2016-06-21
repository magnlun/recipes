from rest_framework import viewsets, permissions, mixins
from django.db.models import F

from .permissions import IsOwnerOrReadOnly
from .serializers import *
from .filters import *

from django.contrib.auth.models import User


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.annotate(sec_time=F('time')*F('time_unit__seconds'))
    serializer_class = RecipeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RecipeFilter

    def get_serializer(self, *args, **kwargs):
        request = self.get_serializer_context()['request']

        if 'fields' in request.query_params and request.query_params['fields']:
            kwargs['fields'] = request.query_params['fields'].split(',')

        return super(RecipeViewSet, self).get_serializer(*args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class QuantityViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Quantity.objects.all()
    serializer_class = QuantitySerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)


class MomentViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Moment.objects.all()
    serializer_class = MomentSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
