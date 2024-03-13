from django.urls import path
from .views import BannerListCreateView, BannerRetrieveUpdateDestroyView,ProductListCreateView,ProductRetrieveUpdateDestroyView


urlpatterns = [
    path('banners/', BannerListCreateView.as_view(), name='banner-list-create'),
    path('banners/<int:pk>/', BannerRetrieveUpdateDestroyView.as_view(), name='banner-retrieve-update-destroy'),
    path('products/', ProductListCreateView.as_view(), name='banner-retrieve-update-destroy'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='banner-retrieve-update-destroy'),
]
