
# virtual_trail/views.py
from django.shortcuts import render
from rest_framework import generics
from virtual_trail.models import Product, VirtualTrailRoom
from .serializers import ProductSerializer, VirtualTrailRoomSerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class VirtualTrailRoomListView(generics.ListCreateAPIView):
    queryset = VirtualTrailRoom.objects.all()
    serializer_class = VirtualTrailRoomSerializer

class VirtualTrailRoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VirtualTrailRoom.objects.all()
    serializer_class = VirtualTrailRoomSerializer
def home_view(request):
    return render(request, 'home.html')