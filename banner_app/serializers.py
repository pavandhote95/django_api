from rest_framework import serializers
from .models import Banner, Product

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
     
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
     
        fields = '__all__'

