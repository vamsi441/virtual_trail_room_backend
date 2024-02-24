# virtual_trail/urls.py
from django.urls import path
from .views import ProductListView, ProductDetailView, VirtualTrailRoomListView, VirtualTrailRoomDetailView
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    # Add other paths as needed
]
urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('virtual-trail-rooms/', VirtualTrailRoomListView.as_view(), name='virtual-trail-room-list'),
    path('virtual-trail-rooms/<int:pk>/', VirtualTrailRoomDetailView.as_view(), name='virtual-trail-room-detail'),
]
