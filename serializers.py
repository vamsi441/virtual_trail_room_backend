
# virtual_trail/serializers.py
from rest_framework import serializers
from .models import Product, VirtualTrailRoom

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class VirtualTrailRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualTrailRoom
        fields = '__all__'
