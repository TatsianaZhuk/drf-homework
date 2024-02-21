from django.urls import path, include
from . import views
from rest_framework import routers
from .views import FlowerViewSet

router = routers.DefaultRouter()
router.register('flowers', FlowerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls'))
]