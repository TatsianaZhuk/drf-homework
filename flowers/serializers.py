from .models import Flower
from rest_framework import serializers


class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ('__all__')

