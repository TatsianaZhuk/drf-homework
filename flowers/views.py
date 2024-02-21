from .models import Flower
from .serializers import FlowerSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import AllForAdminOtherReadOnly
from rest_framework import filters


class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = (AllForAdminOtherReadOnly, )
    filter_backends = [filters.OrderingFilter]
    search_fields = ['name', 'color', 'season']
